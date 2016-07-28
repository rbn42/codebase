#include <QApplication>
#include <QCommandLineParser>
#include <QDir>
#include <QFont>
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QSettings>
#include <QtDebug>
#include <stdlib.h>

#include <QApplication>
#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char* argv[])
{
    QGuiApplication app(argc, argv);
    QFont font("monaco,setofont,wenquanyi micro hei");
    //font.setStyleStrategy(QFont::NoFontMerging);
    font.setFixedPitch(false);
    font.setKerning(false);
    font.setOverline(false);
    font.setStrikeOut(false);
    font.setPointSize(32);
    QQmlApplicationEngine engine;
    engine.rootContext()->setContextProperty("current_path", font);
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));

    return app.exec();
}
