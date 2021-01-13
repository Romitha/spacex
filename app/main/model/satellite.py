from .. import db


class Satellite(db.Model):
    """This class represents the satellite table."""

    __tablename__ = 'satellite'

    id = db.Column(db.Integer, primary_key=True)
    satellite_name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    is_active = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, satellite_name, address, is_active, user_id):
        self.satellite_name = satellite_name
        self.address = address
        self.is_active = is_active
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Satellite.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Device '{}'>".format(self.mac_address)
