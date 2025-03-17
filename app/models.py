from .extensions import db
from datetime import datetime, timezone

# User table
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

# Roles table
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

# Spaces table
class Space(db.Model):
    __tablename__ = 'spaces'
    SpaceID = db.Column(db.Integer, primary_key=True)
    SpaceName = db.Column(db.String(255), nullable=False)
    Location = db.Column(db.String(255), nullable=False)
    Capacity = db.Column(db.BigInteger, nullable=False)
    Type = db.Column(db.String(50), nullable=False)
    CreatedAt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Space {self.SpaceName}>'

# Fixed_Assets table
class FixedAsset(db.Model):
    __tablename__ = 'fixed_assets'
    AssetID = db.Column(db.Integer, primary_key=True)
    AssetName = db.Column(db.String(255), nullable=False)
    SerialNumber = db.Column(db.String(255), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Vendor = db.Column(db.String(255), nullable=False)
    PurchasePrice = db.Column(db.Numeric(10, 2), nullable=False)
    DateOfPurchase = db.Column(db.Date, nullable=False)
    PhysicalLocation = db.Column(db.String(255), nullable=False)
    DepartmentOwner = db.Column(db.String(255), nullable=False)
    DepreciationRate = db.Column(db.Numeric(5, 2), nullable=False)
    DepreciationStartDate = db.Column(db.Date, nullable=False)
    CreatedAt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  
    UpdatedAt = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)) 

    def __repr__(self):
        return f'<FixedAsset {self.AssetName}>'

# Assignments table
class Assignment(db.Model):
    __tablename__ = 'assignments'
    ItemID = db.Column(db.Integer, primary_key=True)
    Quantity = db.Column(db.Integer, nullable=False)
    AssignmentDate = db.Column(db.Date, nullable=False)
    AssignedTo = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Assignment {self.ItemID}>'

# Assignment_History table
class AssignmentHistory(db.Model):
    __tablename__ = 'assignment_history'
    AssignmentID = db.Column(db.Integer, primary_key=True)
    ItemID = db.Column(db.Integer, nullable=False)
    AssignedTo = db.Column(db.String(255), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    Location = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<AssignmentHistory {self.AssignmentID}>'