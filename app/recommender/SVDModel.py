import pandas as pd
from surprise import SVD
from surprise import Dataset
from surprise import Reader
import joblib
from app.models.DuLieuHuanLuyen import DuLieuHuanLuyen

# Train model with SVD algorithm
def TrainModel ():
    #Load data from db
    data_train = DuLieuHuanLuyen.getAll()
    df_train = pd.DataFrame([(r.MSSV, r.MaMonHoc, r.Diem) for r in data_train], 
                          columns=['MSSV', 'MaMonHoc', 'Diem'])
    reader = Reader(rating_scale=(0, 10))
    data = Dataset.load_from_df(df_train[['MSSV', 'MaMonHoc', 'Diem']], reader)
    algo = SVD()
    trainset = data.build_full_trainset()
    # fit the algorithm on the trainset 
    algo.fit(trainset)
    # save model to file
    joblib.dump(algo, './app/recommender/svdModel.pkl')


# Predict score
def GetPredictions(DSMonHoc, MSSV):
    # get model from file
    model = joblib.load('./app/recommender/svdModel.pkl')
    # get predictions
    predictions = []
    for MonHoc in DSMonHoc:
        prediction = model.predict(uid = MSSV, iid = MonHoc)
        predictions.append(prediction)
    return predictions