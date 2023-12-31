# DataAnalytics - Projektmappe Grab, Klöble, Ricker

Die folgende Projektmappe baut auf dem Kaggle Datensatz ['Smoking and Drinking Dataset with body signal'](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset) auf.

Erläuterungen und weitere Aspekte werden in der Dokumentation dargelegt.

Gegliedert wurde das Projekt in die Mindestanforderungen im Ordner 'DataAnalytics > Projekt > Anforderungen' und in ein finales Notebook 'Projektmappe.ipynb' für unseren UseCase.

## Erläuterung der Ordnerstruktur

DataAnalytics

> Beinhaltet GitHub-relevante Dateien und den [Projekt](Projekt) Ordner

DataAnalytics > Projekt

> Beinhaltet die [Projektmappe](Projekt/Projektmappe.ipynb) (unser finaler Use-Case des Moduls), sowie die Ordner [Daten](Projekt/Daten) und [Anforderungen](Projekt/Anforderungen)

DataAnalytics > Projekt > Daten

> Im Repository ist der Ordner 'Daten' leer. Dieser muss mit dem Dataset ([smoking_driking_dataset_Ver01.csv](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset)) befüllt werden, sodass die Notebooks funktionieren. Weitere Details hierzu im nächsten Kapitel, der Bedienungsanleitung.

DataAnalytics > Projekt > Anforderungen

> Dieser Ordner beinhaltet die Notebooks zu allen Anforderungen, eine [requirements.txt Datei](Projekt/Anforderungen/requirements.txt) zum Definieren der Pipeline, ein [init_notebook](Projekt/Anforderungen/init_notebook.py) für globale Funktionen sowie die Ordner Logs und Modelle.

DataAnalytics > Projekt > Anforderungen > Logs

> Beinhaltet [Log-Dateien](Projekt/Anforderungen/Logs) aus den Anforderungen.

DataAnalytics > Projekt > Anforderungen > Modelle

> Beinhaltet trainierte [Modelle](Projekt/Anforderungen/Modelle) aus den Anforderungen.

## Bedienungsanleitung

Dass die Jupyter Notebooks dieses Repositories funktionieren, müssen zunächst wenige Schritte durchgeführt werden:

1. Download des [Datasets](https://www.kaggle.com/datasets/sooyoungher/smoking-drinking-dataset) und speichern im Ordner [DataAnalytics > Projekt > Daten](Projekt/Daten) mit dem Namen 'smoking_driking_dataset_Ver01.csv'.

2. Starten der Codezellen des Notebooks [0_StartUp.ipynb](Projekt/Anforderungen/0_StartUp.ipynb).

Nun können die Notebooks ausgeführt werden.