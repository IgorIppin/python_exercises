# Creación de una agenda de contactos

import csv

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        # Iteracion con enumerate para obtener el indice y el contacto
        print(name)
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
        
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, original_name, name, phone, email):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == original_name.lower():
                self._contacts[idx].name = name
                self._contacts[idx].phone = phone
                self._contacts[idx].email = email
                self._save()
                break
        else:
            self._not_found()

    @staticmethod
    def _not_found():
        print('¡Contacto no encontrado!')

    @staticmethod
    def _print_contact(contact):
        print('---------------------------')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---------------------------')

    # Guardar la información en un csv
    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            # Añadir al csv los nombre de columna
            writer.writerow(('name', 'phone', 'email'))

            # Rellena rel excel con los datos del usuario
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue

            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Nombre del contacto: '))
            phone = str(input('Teléfono del contacto: '))
            email = str(input('Email del contacto: '))

            # Añadir contacto
            contact_book.add(name, phone, email)

        elif command == 'ac':
            original_name = str(input('Nombre contacto: '))
            name = str(input('Nombre nuevo del contacto: '))
            phone = str(input('Teléfono nuevo del contacto: '))
            email = str(input('Email nuevo del contacto: '))
            contact_book.update(original_name, name, phone, email)

        elif command == 'b':
            name = str(input('Nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('Bienvenido a la agenda 2020')
    run()
