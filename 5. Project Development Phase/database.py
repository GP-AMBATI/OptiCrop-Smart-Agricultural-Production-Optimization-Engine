from datetime import datetime
from pathlib import Path

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        Text, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "database.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    predictions = relationship("Prediction", back_populates="user")


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    n = Column(Float, nullable=False)
    p = Column(Float, nullable=False)
    k = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    ph = Column(Float, nullable=False)
    rainfall = Column(Float, nullable=False)
    predicted_crop = Column(String(120), nullable=False)
    confidence = Column(Float, nullable=False)
    probability_json = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="predictions")
    report = relationship("Report", back_populates="prediction", uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "n": self.n,
            "p": self.p,
            "k": self.k,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "ph": self.ph,
            "rainfall": self.rainfall,
            "predicted_crop": self.predicted_crop,
            "confidence": self.confidence,
            "probabilities": self.probability_json,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
        }


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    prediction_id = Column(Integer, ForeignKey("predictions.id"), nullable=False)
    summary = Column(Text, nullable=True)
    downloaded_at = Column(DateTime, default=datetime.utcnow)

    prediction = relationship("Prediction", back_populates="report")


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    source = Column(String(256), nullable=False)
    description = Column(Text, nullable=True)
    records = Column(Integer, nullable=True)


class MLModel(Base):
    __tablename__ = "mlmodels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    version = Column(String(80), nullable=True)
    path = Column(String(256), nullable=False)
    accuracy = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_or_create_guest_user(db_session):
    user = db_session.query(User).filter(User.username == "guest").first()
    if user:
        return user
    user = User(username="guest", email="guest@opticropsystem.local")
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def log_prediction(db_session, user_id, features, crop_name, confidence, probabilities):
    probability_json = str(probabilities)
    prediction = Prediction(
        user_id=user_id,
        n=features[0],
        p=features[1],
        k=features[2],
        temperature=features[3],
        humidity=features[4],
        ph=features[5],
        rainfall=features[6],
        predicted_crop=crop_name,
        confidence=confidence,
        probability_json=probability_json,
    )
    db_session.add(prediction)
    db_session.commit()
    db_session.refresh(prediction)
    return prediction
