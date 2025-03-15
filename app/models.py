from .extensions import db
from datetime import datetime

#user table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship('Role', back_populates='users', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
#Roles table
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    permissions = db.relationship('Permission', secondary='role_permission', back_populates='roles', lazy=True)
    users = db.relationship('User', back_populates='role', lazy=True)
    
class RolePermission(db.Model):
    __tablename__ = 'role_permission'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)
    

    
class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)  
    roles = db.relationship('Role', secondary='role_permission', back_populates='permissions', lazy=True)


class Vendor(db.Model):
    __tablename__ = 'vendors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    bio = db.Column(db.Text)
    kra_pin = db.Column(db.String(20), nullable = False)
    status = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    contact_name = db.Column(db.String(50), nullable = False)
    contact_email = db.Column(db.String(100), nullable = False)
    contact_number = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(50),nullable=False)
    county = db.Column(db.String(20),nullable=False)
    country = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(30))
    postal_code = db.Column(db.String(30))
    bank_name = db.Column(db.String(255), nullable=False)
    account_number = db.Column(db.String(255), nullable=False)
    mpesa_paybill = db.Column(db.String(255))
    buy_goods_till = db.Column(db.String(255))

    def __repr__(self):
        return f"<Vendor {self.name}>"

###vendor douments
# it contains the douments for each vendor
# one vendor can have many documents(1:m)###

class Vendor_Doc:
    __tablename__ = 'vendor_docs'
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    document_name = db.Column(db.String(50),nullable=False)
    doc_type = db.Column(db.String(20),nullable=False)

#orders table
class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_name = db.Column(db.String(50), nullable=False)
    order_description = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'), nullable=False)
    vat = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    date_ordered = db.Column(db.Date, nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    dispatch_status = db.Column(db.String(50), nullable=False)
    delivery_charges = db.Column(db.Float, nullable=True)
    reason = db.Column(db.String(50), nullable=True)
    initialiser = db.Column(db.String(50), nullable=True)
 
    received = db.relationship('Received', back_populates='order', cascade="all, delete-orphan", lazy=True)
    vendor = db.relationship('Vendor', back_populates='orders')

#partially received goods tabe
class Received(db.Model):
    __tablename__ = 'received'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    received_quantity = db.Column(db.Integer, nullable=False)
    date_received = db.Column(db.Date, nullable=False)

    order = db.relationship('Orders', back_populates='received')