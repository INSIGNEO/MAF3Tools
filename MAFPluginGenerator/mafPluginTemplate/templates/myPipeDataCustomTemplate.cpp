/*
 *  myPipeDataCustom.cpp
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 16/04/10.
 *  Copyright 2011 SCS-B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#include "myPipeDataCustom.h"
#include <mafVME.h>
#include <mafDataSet.h>

using namespace mafCore;
using namespace mafResources;
using namespace mafPlugin{{ pluginName }};

myPipeDataCustom::myPipeDataCustom(const QString code_location) : mafPipeData(code_location) {
}

myPipeDataCustom::~myPipeDataCustom() {
}

bool myPipeDataCustom::acceptObject(mafCore::mafObjectBase *obj) {
    mafVME *vme = qobject_cast<mafVME*>(obj);
    if(vme != NULL) {
        QString dataType = vme->dataSetCollection()->itemAtCurrentTime()->externalDataType();
        if(dataType == "SOMETHING_EDIT_HERE") {
            return true;
        }
    }
    return false;
}

void myPipeDataCustom::updatePipe(double t) {
    if (inputList()->size() == 0) {
        return;
    }

    mafDataSet *inputDataSet = dataSetForInput(0, t);
    if(inputDataSet == NULL) {
        return;
    }

    //Get data contained in the mafProxy

    Superclass::updatePipe(t);
}
