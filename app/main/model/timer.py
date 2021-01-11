from .. import db


class Timer(db.Model):
    """This class represents the Setup table."""

    __tablename__ = 'timer'

    id = db.Column(db.Integer, primary_key=True)
    timer_duration = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1024))
    mac_address = db.Column(db.String(455))
    is_complete = db.Column(db.Integer, nullable=False)
    is_cancel = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    device_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    

    def __init__(self, timer_duration, description, mac_address, is_complete, is_cancel, user_id, device_id):

        self.timer_duration = timer_duration
        self.description = description
        self.mac_address = mac_address
        self.is_complete = is_complete
        self.is_cancel = is_cancel
        self.user_id = user_id
        self.device_id = device_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Timer.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Timer '{}'>".format(self.mac_address)
