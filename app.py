"""
Simple Flask CRUD Application with Security Features
"""
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from forms import LoginForm, ContactForm
from models import db, User, Contact
import bleach

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CSRF Protection
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_TIME_LIMIT'] = None

# Secure Session Management
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

# Initialize extensions
db.init_app(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

# Create database tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    form = LoginForm()
    
    if form.validate_on_submit():
        username = bleach.clean(form.username.data.strip())
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            session.permanent = True
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!')
    
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if request.method == 'POST':
        username = bleach.clean(request.form.get('username', '').strip())
        password = request.form.get('password', '')
        
        if not username or not password:
            flash('Username and password required!')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists!')
            return redirect(url_for('register'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    """Dashboard"""
    if 'user_id' not in session:
        flash('Please login first!')
        return redirect(url_for('login'))
    
    contacts = Contact.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', contacts=contacts)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Add contact"""
    if 'user_id' not in session:
        flash('Please login first!')
        return redirect(url_for('login'))
    
    form = ContactForm()
    
    if form.validate_on_submit():
        name = bleach.clean(form.name.data.strip())
        email = bleach.clean(form.email.data.strip())
        phone = bleach.clean(form.phone.data.strip())
        address = bleach.clean(form.address.data.strip())
        
        new_contact = Contact(
            name=name,
            email=email,
            phone=phone,
            address=address,
            user_id=session['user_id']
        )
        
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('contact.html', form=form)


@app.route('/delete/<int:contact_id>', methods=['POST'])
def delete_contact(contact_id):
    """Delete contact"""
    if 'user_id' not in session:
        flash('Please login first!')
        return redirect(url_for('login'))
    
    contact = Contact.query.filter_by(id=contact_id, user_id=session['user_id']).first()
    
    if contact:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted!')
    
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('index'))


# Secure Error Handling
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(403)
def forbidden_error(error):
    """Handle 403 errors"""
    return render_template('errors/403.html'), 403


@app.errorhandler(400)
def bad_request_error(error):
    """Handle 400 errors"""
    return render_template('errors/400.html'), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
