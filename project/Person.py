
class Person:
    name = []

    # Store name
    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    # Retrieve name
    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]
if __name__ == '__main__':
    person = Person()
    print('User Stuart has been added with id', person.set_name('Stuart'))
    print('User associated with id {} is {}'.format(0, person.get_name(0)))
