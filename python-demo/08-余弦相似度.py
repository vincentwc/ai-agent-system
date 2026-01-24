import numpy as np

"""
计算两个向量的余弦相似度（衡量方向的相似性，剔除长度影响）
参数：
    vector1：向量1
    vector2：向量2
返回：
  float：余弦相似度结果（范围义，越小越相似[-1, 1],越接近1方向越一致）
公式：
  cos(a, b) = a . b / (|a| * |b|)ƒ
相似度：

"""


def get_dot(vec_a, vec_b):
    """计算两个向量的点积,2个向量的点积等于两个向量对应元素相乘之和"""
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量的维度必须相同")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b
    return dot_sum


def get_norm(vec):
    """计算向量的模: 向量各元素平方和的平方根"""
    sum_square = 0
    for i in vec:
        sum_square += i * i

    return np.sqrt(sum_square)


def cosine_similarity(vector1, vector2):
    """计算两个向量的余弦相似度: 余弦相似度 = 点积 / (向量a模 * 向量b模)"""
    dot_product = get_dot(vector1, vector2)
    norm_a = get_norm(vector1)
    norm_b = get_norm(vector2)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("向量的模不能为零")

    cosine_sim = dot_product / (norm_a * norm_b)
    return cosine_sim


if __name__ == "__main__":
    vector1 = [0.5, 0.5]
    vector2 = [0.7, 0.7]
    vector3 = [-0.6, -0.5]
    print(cosine_similarity(vector1, vector2))
    print(cosine_similarity(vector1, vector3))
    print(cosine_similarity(vector2, vector3))
