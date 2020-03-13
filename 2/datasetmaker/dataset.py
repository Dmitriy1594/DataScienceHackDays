from googletrans import Translator
import csv
import pandas as pd


def translate(msg=None):
    translator = Translator()
    translated = translator.translate(msg, dest='ru', src='en')
    return str(translated.text)


def maker(path_with_name, path_with_name_new, start_id=0):
    train = pd.read_csv(path_with_name, sep=",")
    fieldnames = list(train.columns.values)

    with open(f'{path_with_name_new}', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        i = 0
        with open(f'{path_with_name}', 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if i < start_id:
                    i += 1
                elif i >= start_id:
                    d = row

                    print(f"Продукт:\n{d['Shrt_Desc']}\n")
                    ru_product = translate(d['Shrt_Desc'])
                    print(f"Продукт:\n{ru_product}\n")
                    cl = input(
                        "Введите тип продукта:\n1. Хлебобулочное изделие\n2. Жидкость\n3. Молочная продукция\n4. Мясная продукция\n5. Овощи/фрукты\nОтвет: ")

                    d['Class'] = cl
                    print('\n')

                    del d['']
                    # print(d)
                    writer.writerow(d)

if __name__ == '__main__':
    path_with_name = '/docs/csv/gramms_test_valid.csv'
    path_with_name_new = 'dataset.csv'
    start_id = 260
    maker(path_with_name, path_with_name_new, start_id)
#
