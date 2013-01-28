/*
 *  myInteractorCustom.cpp
 *  mafPluginVTK
 *
 *  Created by Daniele Giunchi - Paolo Quadrani on 7/7/11.
 *  Copyright 2011 SCS-B3C.s All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#include <QMouseEvent>

#include "myInteractorCustom.h"

using namespace mafPlugin{{ pluginName }};

myInteractorCustom::myInteractorCustom(const QString code_location) : mafResources::mafInteractor(code_location) {

}

myInteractorCustom::~myInteractorCustom() {

}

void myInteractorCustom::mousePress(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e) {
    
    switch(((QMouseEvent *)e)->button()) {
        case Qt::LeftButton:
            break;
        case Qt::MidButton:
            break;
        case Qt::RightButton:
            break;
        default:
            break;
    }
}

void myInteractorCustom::mouseRelease(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e) {
    switch(((QMouseEvent *)e)->button()) {
        case Qt::LeftButton:
            break;
        case Qt::MidButton:
            break;
        case Qt::RightButton:
            break;
        default:
            break;
    }
}

void myInteractorCustom::mouseMove(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e) {
    
}

void myInteractorCustom::mouseWheelForward(unsigned long modifiers, QEvent *e) {
}

void myInteractorCustom::mouseWheelBackward(unsigned long modifiers, QEvent *e) {
}
