from facenet.src import facenet
import tensorflow as tf
from app.domain.face.align import detect_face


def getModel():
    sess = tf.Session()
    # read pnet, rnet, onet models from align directory and files are det1.npy, det2.npy, det3.npy
    pnet, rnet, onet = detect_face.create_mtcnn(sess, 'app/models/align')

    # read 20170512-110547 model file downloaded from https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk
    facenet.load_model("app/models/model/tfmodel.pb")

    # Get input and output tensors
    images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
    embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
    phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

    return (sess, pnet, rnet, onet,images_placeholder, embeddings, phase_train_placeholder )