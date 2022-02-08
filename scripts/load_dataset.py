from load_mat import load_mat_file
from load_cardio import load_cardio
from load_kdd import load_kdd
from load_spambase import load_spambase
from load_thyroid import load_thyroid
from load_shuttle import load_shuttle


def load_dataset(dataset, setting):

    if(dataset == "arrhythmia"):
        return load_mat_file("data/arrhythmia.mat", setting)
    if(dataset == "cardio"):
        return load_cardio("data/Cardiotocography.npy", setting)
    if(dataset == "spambase"):
        return load_spambase("data/SpamBase.npy", setting)
    if(dataset == "thyroid"):
        return load_thyroid("data/Thyroid.npy", setting)
    if(dataset == "kddcup"):
        return load_kdd("data/kdd_cup.npz", setting)
    if(dataset == "shuttle"):
        return load_shuttle("data/shuttle.mat", setting)
    if(dataset == "glass"):
        return load_mat_file("data/glass.mat", setting)
    if(dataset == "ionosphere"):
        return load_mat_file("data/ionosphere.mat", setting)
    if(dataset == "letter"):
        return load_mat_file("data/letter.mat", setting)
    if(dataset == "lympho"):
        return load_mat_file("data/lympho.mat", setting)
    if(dataset == "mnist"):
        return load_mat_file("data/mnist.mat", setting)
    if(dataset == "musk"):
        return load_mat_file("data/musk.mat", setting)
    if(dataset == "optdigits"):
        return load_mat_file("data/optdigits.mat", setting)
    if(dataset == "pendigits"):
        return load_mat_file("data/pendigits.mat", setting)
    if(dataset == "pima"):
        return load_mat_file("data/pima.mat", setting)
    if(dataset == "satellite"):
        return load_mat_file("data/satellite.mat", setting)
    if(dataset == "satimage"):
        return load_mat_file("data/satimage-2.mat", setting)
    if(dataset == "vertebral"):
        return load_mat_file("data/vertebral.mat", setting)
    if(dataset == "vowels"):
        return load_mat_file("data/vowels.mat", setting)