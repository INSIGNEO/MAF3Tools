/*
 *  myPipeVisualNode.cpp
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 10/05/11.
 *  Copyright 2011 SCS-B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#include "myPipeVisualCustom.h"
#include <mafVME.h>
#include <mafDataSet.h>
#include <mafDataSetCollection.h>

using namespace mafCore;
using namespace mafResources;
using namespace mafPlugin{{ pluginName }};
using namespace std;

myPipeVisualCustom::myPipeVisualCustom(const QString code_location) : mafPipeVisual(code_location) {
    m_UIFilename = "myPipeVisualNode.ui";
    
    //set an output, a node or an actor
}

myPipeVisualCustom::~myPipeVisualCustom() {

}

bool myPipeVisualCustom::acceptObject(mafCore::mafObjectBase *obj) {
    mafVME *vme = qobject_cast<mafVME*>(obj);
    if(vme != NULL) {
        QString dataType = vme->dataSetCollection()->itemAtCurrentTime()->externalDataType();
        if(dataType.startsWith("SOMETHING_EDIT_HERE" , Qt::CaseSensitive)) {
            return true;
        }
    }
    return false;
}

void myPipeVisualCustom::updatePipe(double t) {
    //Superclass::updatePipe(t); //if inherits

    mafDataSet *data = dataSetForInput(0, t);
    // get proxy

    //Keep ImmediateModeRendering off: it slows rendering
    //m_Mapper->SetImmediateModeRendering(m_ImmediateRendering);
    updatedGraphicObject();
}
