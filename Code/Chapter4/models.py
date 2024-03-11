from typing import Optional
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from werkzeug.security import generate_password_hash, check_password_hash




class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str]= so.mapped_column(sa.String(64),index=True,unique=True)

    email: so.Mapped[str]= so.mapped_column(sa.String(120),index=True,unique=True)

    password_hash: so.Mapped[Optional[str]]= so.mapped_column(sa.String(256))

    posts: so.WriteOnlyMapped['Post']=so.relationship(back_populates='author')
    def __repr__(self):
        return '<User {}>'.format(self.username)

    #the new code

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id: so.Mapped[int]=so.mapped_column(primary_key=True)
    body: so.Mapped[str]=so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime]=so.mapped_column(index=True, default = lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int]=so.mapped_column(sa.ForeignKey(User.id),index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')
    def __repr__(self):
        return '<post {}>'.format(self.body)


