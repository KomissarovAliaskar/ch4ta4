class ContactList(list):
    all_contacts = ['Garik', 'Vazgen', 'Cristiano', 'Afansiy']

    def search_by_name(self,name, second_name, third_name):
        otsorted_list = []
        for i in ContactList.all_contacts:
            if i == name:
                otsorted_list.append(i)
        return otsorted_list

contacts = ContactList()
same_name = contacts.search_by_name('Vazgen', 'Garik', 'Lioneel')
print(same_name)

