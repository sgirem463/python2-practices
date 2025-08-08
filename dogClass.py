''' Practice creating classes and to teach the most common magic methods '''

class Dog:
    'A simple canine class'

    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def bark(self):
        print 'Woof!  %s is barking' % self.name

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('Index out of range')
        return index * 111

    def __call__(self, action):
        if action == 'fetch':
            return '%s is fetching' % self.name
        elif action == 'owner':
            return 'raymond'
        else:
            raise ValueError('Unknown action')

    def __add__(self, other):
        newname = self.name + '~' + other.name
        return Dog(newname)

    def __mul__(self, other):
        newname = '~'.join([self.name] * other)
        return Dog(newname)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return 'I am a dog named %s' % self.name

    def __repr__(self):
        return 'Dog(%r)' % self.name


if __name__ == '__main__':

    d = Dog('Fido')
    e = Dog('Buddy')
    f = Dog('Checkers')
    g = d + e

    d.bark()
    e.bark()
    f.bark()
