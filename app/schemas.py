from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    contact = fields.Str(required=True)
    password = fields.Str(load_only=True, required=True)
    role_id = fields.Int(required=True)

#user instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)
    
class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    permissions = fields.List(fields.Int())

class PermissionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class VendorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    bio = fields.Str()
    kra_pin = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    contact_name = fields.Str(required=True)
    contact_email = fields.Email(required=True)
    contact_number = fields.Str(required=True)
    address = fields.Str(required=True)
    county = fields.Str(required=True)
    country = fields.Str(required=True)
    city = fields.Str()
    postal_code = fields.Str()
    bank_name = fields.Str(required=True)
    account_number = fields.Str(required=True)
    mpesa_paybill = fields.Str()
    buy_goods_till = fields.Str()

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

class VendorDocSchema(Schema):
    id = fields.Int(dump_only=True)
    vendor_id = fields.Int(required=True)
    document_name = fields.Str(required=True)
    doc_type = fields.Str(required=True)

vendor_doc = VendorDocSchema()

class OrdersSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    order_name = fields.Str(required=True)
    order_description = fields.Str(required=True)
    name = fields.Str(required=True)
    cost = fields.Float(required=True)
    vendor_id = fields.Int(required=True)
    vat = fields.Float(required=True)
    quantity = fields.Int(required=True)
    status = fields.Str(required=True)
    date_ordered = fields.Date(required=True)
    payment_status = fields.Str(required=True)
    dispatch_status = fields.Str(required=True)
    delivery_charges = fields.Float()
    reason = fields.Str()
    initialiser = fields.Str()

class ReceivedSchema(Schema):
    id = fields.Int(dump_only=True)
    order_id = fields.Int(required=True)
    received_quantity = fields.Int(required=True)
    date_received = fields.Date(required=True)

#Order Instances
order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)

#received partially instances
received_schema= ReceivedSchema()
receiveds_schema= ReceivedSchema(many=True)
