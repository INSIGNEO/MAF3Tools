/*
 *  myInteractorCustom.h
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 7/7/11.
 *  Copyright 2012 SCS-B3C.s All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYINTERACTOR_H
#define MYINTERACTOR_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include <mafInteractor.h>

// Foundation Class forwarding list

namespace mafPlugin{{ pluginName }} {

/**
Class name: MyInteractor
This class represent an interactor implementing a picking operation.
*/

class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} myInteractorCustom : public mafResources::mafInteractor {
    Q_OBJECT
    /// typedef macro.
    mafSuperclassMacro(mafResources::mafInteractor);

public:
    /// Object constructor.
    myInteractorCustom(const QString code_location = "");

public Q_SLOTS:
    /// Called when the any mouse button is pressed
    /*virtual*/ void mousePress(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e);

    /// Called when the any mouse button is released
    /*virtual*/ void mouseRelease(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e);

    /// Called when mouse is moved
    /*virtual*/ void mouseMove(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e);

    /// called when the wheel is moving forward.
    /*virtual*/ void mouseWheelForward(unsigned long modifiers, QEvent *e);

    /// called when the wheel is moving backward.
    /*virtual*/ void mouseWheelBackward(unsigned long modifiers, QEvent *e);

protected:
    /// Object destructor.
    /* virtual */~myInteractorCustom();

private:
    // variables
};


} // namespace mafPlugin{{ pluginName }}

#endif // MYINTERACTORCUSTOM_H
