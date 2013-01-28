/*
 *  myOperationCustom.h
 *  mafPluginVTK
 *
 *  Created by Roberto Mucci on 12/07/11.
 *  Copyright 2011 SCS-B3C.s All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYOPERATIONCUSTOM_H
#define MYOPERATIONCUSTOM_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include <mafOperation.h>

// Foundation Class forwarding list

namespace mafPlugin{{ pluginName }} {

/**
Class name: myOperationCustom
This class represent an operation which add landamrk on a surface.
*/

class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} myOperationCustom : public mafResources::mafOperation {
    Q_OBJECT
    /// typedef macro.
    mafSuperclassMacro(mafResources::mafOperation);

    //Q_PROPERTY(double radius READ radius WRITE setRadius)

public Q_SLOTS:
    /// Execute the operation.
    /*virtual*/ void execute();
    
    /// Allows to call the piece of algorithm that is needed to restore the previous state of the operation's execution.
    /*virtual*/ void unDo();
    
    /// Allows to call the piece of algorithm that is needed to apply the operation again.
    /*virtual*/ void reDo();
    
    /// Called when a VME has been picked.
    /*virtual*/ void vmePicked(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj, QEvent *e);
    
    /// Set operation parameters.
    /*virtual*/ void setParameters(QVariantList parameters);
        
private Q_SLOTS:
    
Q_SIGNALS:
    /// Signal for VME picked.
    void vmePickedSignal(double *pickPos, unsigned long modifiers, mafCore::mafObjectBase *obj);

public:
    /// Object constructor.
    myOperationCustom(const QString code_location = "");

    /// Accept function
    static bool acceptObject(mafCore::mafObjectBase *obj);

    /// Initialize the operation. Put here the initialization of operation's parameters.
    /*virtual*/ bool initialize();
    
protected:
    /// Terminate the operation's execution.
    /*virtual*/ void terminated();

    /// Object destructor.
    /* virtual */~myOperationCustom();

private:
    /// Initialize connection between signals and slots.
    void initializeConnections();

    /// Create chosen surface.
    void internalUpdate();
};

/////////////////////////////////////////////////////////////
// Inline methods
/////////////////////////////////////////////////////////////

} // namespace mafPlugin{{ pluginName }}

#endif // MYOPERATIONCUSTOM_H
