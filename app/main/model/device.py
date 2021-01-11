from .. import db


class Device(db.Model):
    """This class represents the mst_form table."""

    __tablename__ = 'device'

    id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(255))
    mac_address = db.Column(db.String(255))
    is_active = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, device_name, mac_address, is_active, user_id):
        self.device_name = device_name
        self.mac_address = mac_address
        self.is_active = is_active
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Device.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Device '{}'>".format(self.mac_address)
