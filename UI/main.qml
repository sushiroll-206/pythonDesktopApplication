import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    title: "Monaco Clock"

    // Making application window frameless
    // flags: Qt.FramelessWindowHint | Qt.Window

    property string currTime: "00:00:00"
    property QtObject backend

    Rectangle {
        anchors.fill: parent

        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: ".images/monaco.jpg"
            fillMode: Image.PreserveAspectCrop
        }

        Text {
            anchors.centerIn: parent
            horizontalAlignment: Text.AlignHCenter
            text: currTime
            font.pixelSize: 100
            font.family: "Monaco"
            color: "white"

            width: implicitWidth
            height: implicitHeight
        }
    }

    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg
        }
    }
}