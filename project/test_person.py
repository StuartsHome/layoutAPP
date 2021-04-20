import unittest

from project.Person import Person as PersonClass

class Test(unittest.TestCase):
    # inherits unittest.TestCase

    person = PersonClass()   # instantiate the Person Class
    user_id = []                    # variable that stores obtained user_id
    user_name = []                  # variable that stores person name

    def test_0_set_name(self):
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.person.set_name(name)
            self.assertIsNone(user_id)  # check if null
            self.user_id.append(user_id)
    
    def test_1_get_name(self):
        length = len(self.user_id)
        for i in range(6):
            if i < length:
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                self.assertEqual('There is no such user', self.person.get_name(i))


    
if __name__ == '__main__':
    unittest.main()
    # python -m unittest project/test_person.py