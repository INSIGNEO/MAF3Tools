/*
 *  myOperationCustom.cpp
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 12/07/11.
 *  Copyright 2011 SCS-B3C.s All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#include "myOperationCustom.h"
#include <mafVME.h>
#include <mafDataSet.h>

using namespace mafPlugin{{ pluginName }};
using namespace mafResources;
using namespace mafEventBus;
using namespace mafCore;

myOperationCustom::myOperationCustom(const QString code_location) : mafOperation(code_location){
    //set multi-threaded to off
    m_MultiThreaded = false;

    m_UIFilename = "myOperationCustom.ui";
    setObjectName("myOperationCustom");
}

bool myOperationCustom::initialize() {
    bool result = Superclass::initialize();

    return result;
}

bool myOperationCustom::acceptObject(mafCore::mafObjectBase *obj) {
    return obj != NULL;
}

myOperationCustom::~myOperationCustom(){
}

void myOperationCustom::vmePicked(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e) {
}

void myOperationCustom::execute() {
    m_Status = mafOperationStatusExecuting;
    // do something
    Q_EMIT executionEnded();
}

void myOperationCustom::terminated() {
    if (m_Status == mafOperationStatusCanceled || m_Status == mafOperationStatusAborted) {
        unDo();
    }
}

void myOperationCustom::unDo() {
}

void myOperationCustom::reDo() {
}

void myOperationCustom::setParameters(QVariantList parameters) {
    REQUIRE(parameters.count() != 0);
    //m_Parameter = parameters.at(0).toDouble();

}

void myOperationCustom::internalUpdate() {
}
