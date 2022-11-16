import numpy as np
import faiss
from timeit import default_timer as timer
from datetime import timedelta



np.random.seed(1234)


def basic_explorations():
  # Euclidean-distance 
  a = np.random.rand(768, 1)
  b = np.random.rand(768, 1)
  dist = np.linalg.norm(a-b)
  print(dist)

  # Faiss Index
  documents = np.random.random((10000, 768)).astype('float32')  # 10k documents with 768-dim vectors
  index = faiss.IndexFlatL2(768)  # exact-search (exhaustive)
  print(index.is_trained)
  index.add(documents)
  print(index.ntotal)
  k = 4
  D, I = index.search(np.random.random((1, 768)).astype('float32'), k)
  print(I[0])
  print(D)

  ## non-exhaustive search; IndexHNSWFlat
  hnsw_m = 32  # The number of neighbors for HNSW. This is typically 32
  documents = np.random.random((100000, 768)).astype('float32')  # 10k documents with 768-dim vectors
  # start = timer()
  # index = faiss.IndexHNSWFlat(768, hnsw_m)  # exact-search (exhaustive)
  # print(index.is_trained)
  # index.add(documents)
  # print(index.ntotal)
  # end = timer()
  # print("time it took to build index:", timedelta(seconds=end-start))  ## took 25 minutes to build

 





# TODO: 
  # try first on a lambda-instance
    # start with one-gpu first; all embeddings at once? 




