import numpy as np
import pandas as pd


np.set_printoptions(precision=3, suppress=True)

# 分解する行列
c = np.array([[1,1,1],[1,0,0,],[1,0,0],[0,1,1],[0,1,0],[0,0,1]])

# 特異値行列Σ(sigma) → 右特異行列V(v) → 左特異行列U(u) の順に求める

# C^TCの固有値と固有ベクトルの計算
ctc = np.dot(c.T, c)
eigen_values, eigen_vectors = np.linalg.eig(ctc)

# 特異値の計算
singular_values = np.sqrt(eigen_values)
singular_index = np.argsort(singular_values)[::-1]

# 特異値行列の計算
sigma = np.diag(singular_values[singular_index])

# 右特異行列の計算
v = eigen_vectors[:,singular_index]

# 左特異行列の計算
u = np.array([np.dot(c, v[:,i]) / sigma.diagonal()[i] for i in range(len(sigma.diagonal()))]).T

# U_kの計算(k列目以降を削除)
u_k = np.delete(u, range(k, u.shape[1]), axis=1)

# Σ_kの計算(k×k行列にする)
sigma_k = np.delete(sigma, range(k, sigma.shape[0]), axis=0)
sigma_k = np.delete(sigma_k, range(k, sigma.shape[1]), axis=1)

# V_kの計算(k列目以降を削除
v_k = np.delete(v, range(k, v.shape[1]), axis=1)

c_k = u_k.dot(sigma_k.dot(v_k.T))
