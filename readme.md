# Untiplagiat system

Система антиплагиата на основе обученной модели машинного обучения Random Forest.
Обученная модель находится в файле model.pkl

Для запуска приложения, которое выставит оценку похожести кода:
1. скопируте файлы проекта в отдельную директорию 
(model.pkl большой, скачайте его по ссылке https://drive.google.com/file/d/1ZtFh8P2sTIH5Yni8y0r-M-287c5_XUvL/view?usp=share_link)
2. убедитесь что у вас установлен Python (3.6 - 3.8) и необходимые библиотки (файл requrements.txt)
3. предварительно создайте папки files, plagiat1, plagiat2.
3. запустите скрипт командой python3 compare.py input.txt scores.txt --model model.pkl 
4. если необходимо обучить модель заново и сгенерировать файл model.pkl запустите команду python3 train.py files plagiat1 plagiat2 --model model.pkl 

Если возникли вопросы, то их можно задать по скайпу bam271074
