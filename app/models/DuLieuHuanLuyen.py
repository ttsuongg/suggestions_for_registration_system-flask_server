from app import db
import pandas as pd

class DuLieuHuanLuyen(db.Model):
    __tablename__ = 'DuLieuHuanLuyen'

    ID = db.Column(db.Integer, primary_key = True)
    MSSV = db.Column(db.String())
    MaMonHoc = db.Column(db.String())
    Diem = db.Column(db.Float())

    def __init__(self, MSSV, MaMonHoc, Diem):
        self.MSSV = MSSV
        self.MaMonHoc = MaMonHoc
        self.Diem = Diem
    
    def getAll():
        return DuLieuHuanLuyen.query.all()
