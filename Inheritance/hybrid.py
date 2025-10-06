class A:
    def feature_a(self):
        print("features of A")
class B(A):
    def feature_b(self):
        print("feature of B From B")
class C(A):
    def feature_c(self):
        print("feature of C From c")
class D(B,C):
    def feature_d(self):
        print("feature of D From D")

s=D()
s.feature_a()
s.feature_b()
s.feature_c()
s.feature_d()