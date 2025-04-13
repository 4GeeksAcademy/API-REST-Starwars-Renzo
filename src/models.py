from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    firstName: Mapped[str] = mapped_column(nullable=False)
    lastName: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, id, username, firstName, lastName):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName
            #"planetas_favoritos": [favorite.serialize() for favorite in self.planetas_favoritos],
            #"personajes_favoritos": [favorite.serialize() for favorite in self.personajes_favoritos]
        }

class Planetas_favoritos(db.Model):
    __tablename__='planetas_favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    usuario_id: Mapped[str] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped["Usuario"] = relationship("Usuario", backref="planetas_favoritos")

    planetas_id: Mapped[int] = mapped_column(ForeignKey('planetas.id'))
    planetas: Mapped["Planetas"] = relationship()

    def __init__(self, id, usuario_id, planetas_id):
        self.id = id
        self.usuario_id = usuario_id
        self.planetas_id = planetas_id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planetas_id": self.planetas_id
        }

class Personajes_favoritos(db.Model):
    __tablename__='personajes_favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)

    usuario_id: Mapped[str] = mapped_column(ForeignKey('usuario.id'))
    usuario: Mapped["Usuario"] = relationship("Usuario", backref="personajes_favoritos")

    personajes_id: Mapped[int] = mapped_column(ForeignKey('personajes.id'))
    personajes: Mapped["Personajes"] = relationship()

    def __init__(self, id, usuario_id, personajes_id):
        self.id = id
        self.usuario_id = usuario_id
        self.personajes_id = personajes_id

    def serialize(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "personajes_id": self.personajes_id
        }

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    gravity: Mapped[str] = mapped_column()
    diameter: Mapped[str] = mapped_column()
    climate: Mapped[str] = mapped_column()
    terrain: Mapped[str] = mapped_column()

    def __init__(self, id, name, gravity, diameter, climate, terrain):
        self.id = id
        self.name = name
        self.gravity = gravity,
        self.diameter = diameter,
        self.climate = climate,
        self.terrain = terrain

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "diameter": self.diameter,
            "climate": self.climate,
            "terrain": self.terrain
        }


class Personajes(db.Model):
    __tablename__='personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    height: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    birthYear: Mapped[str] = mapped_column()
    eyeColor: Mapped[str] = mapped_column()

    def __init__(self, id, name, height, gender, birthYear, eyeColor):
        self.id = id
        self.name = name
        self.height = height,
        self.gender = gender,
        self.birthYear = birthYear,
        self.eyeColor = eyeColor

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender,
            "birthYear": self.birthYear,
            "eyeColor": self.eyeColor
        }