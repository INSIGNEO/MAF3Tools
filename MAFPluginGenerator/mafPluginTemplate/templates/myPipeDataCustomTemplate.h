/*
 *  myPipeDataCustom.h
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 16/04/10.
 *  Copyright 2011 SCS-B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYDATAPIPECUSTOM_H
#define MYDATAPIPECUSTOM_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include <mafPipeData.h>
#include <mafProxy.h>

// Foundation Class forwarding list

namespace mafPlugin{{ pluginName }} {

// Class forwarding list

/**
 Class name: myPipeDataCustom
 This class allows you to make a thresholding on input image data.
 */
class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} myPipeDataCustom : public mafResources::mafPipeData {
    Q_OBJECT
    //Q_PROPERTY(myProperty myProperty READ myProperty WRITE setMyProperty)
    /// typedef macro.
    mafSuperclassMacro(mafResources::mafPipeData);

public:
    /// Object constructor.
    myPipeDataCustom(const QString code_location = "");

    /// Accept function
    static bool acceptObject(mafCore::mafObjectBase *obj);

public Q_SLOTS:
    /// Allow to execute and update the pipeline when something change
    /*virtual*/ void updatePipe(double t = -1);

protected:
    /// Object destructor.
    /* virtual */ ~myPipeDataCustom();

private:
    // some output
};

} // namespace mafPlugin{{ pluginName }}

#endif // MYDATAPIPECUSTOM_H
