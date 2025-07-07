from mongoengine import BooleanField, Document, EmbeddedDocument, EmbeddedDocumentField, StringField


class Address(EmbeddedDocument):
    street = StringField(required=False)
    number = StringField(required=False)
    district = StringField(required=False)
    city = StringField(required=False)
    state = StringField(required=False)
    zip_code = StringField(required=False)


class Manager(EmbeddedDocument):
    name = StringField(required=True)
    cpf = StringField(required=True)
    email = StringField(required=False)


class AccountingOfficeModel(Document):
    name = StringField(required=True)
    cnpj = StringField(required=True)
    address = EmbeddedDocumentField(Address, required=False)
    phone = StringField(required=True)
    email = StringField(required=False)
    manager = EmbeddedDocumentField(Manager, required=True)
    is_active = BooleanField(required=True)
    created_at = StringField(required=True)
    updated_at = StringField(required=False)
