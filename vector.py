class vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)
        
    def __add__(self, other):       #addition of vectors
        return vector([a+b for a,b in zip(self.components, other.components)])      #zip is used to pair up corresponding numbers from both vecotrs
                      
    def __sub__(self, other):       #subtraction of vectors
        return vector([a-b for a,b in zip(self.components, other.components)])
    
    def dot(self, other):       #dot product of vectors
        return sum(a*b for a,b in zip(self.components, other.components))
    
    def magnitude(self):        #calculate length of vector 
        return sum(x**2 for x in self.components)**0.5
    
    def normalize(self):        #return a unit vector in the same direction as self
        mag = self.magnitude()
        return vector([x/mag for x in self.components])
    
    def cosine_similarity(self, other):         #calcuate how similar the two vectors are by measuring the cosine angle between them 
        return self.dot(other) / (self.magnitude()*other.magnitude())
    
    def __repr__(self):     
        return f"vector({self.components})"
    
    
a = vector([1, 2, 3])       #create a vector with components 1,2,3
b = vector([4,5,6])

print(f"a+b = {a+b}")
print(f"a-b = {a.dot(b)}")
print(f"|a| = {a.magnitude():.4f}")
print(f"cosine similarity  = {a.cosine_similarity(b):.4f}")