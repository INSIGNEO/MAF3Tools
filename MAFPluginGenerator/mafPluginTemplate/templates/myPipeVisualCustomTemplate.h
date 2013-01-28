/*
 *  myPipeVisualCustom.h
 *  mafPluginVTK
 *
 *  Created by Daniele Giunchi on 10/05/11.
 *  Copyright 2009 SCS-B3C. All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYVISUALPIPECUSTOM_H
#define MYVISUALPIPECUSTOM_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include "mafPipeVisual.h"

// Foundation Class forwarding list

namespace mafPlugin{{ pluginName }} {

/**
 Class name: myPipeVisualCustom
 This visual pipe allow to extract a surface from a volume data given a 
 threshold value. The value is extracted according to the scalar values present 
 into the volume data. The iso-surface is extracted in real time*/

class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} myPipeVisualCustom : public mafResources::mafPipeVisual {
    Q_OBJECT
    //Q_PROPERTY(QString contourValue READ contourValue WRITE setContourValue)
    /// typedef macro.
    mafSuperclassMacro(mafResources::mafPipeVisual);
    
public:
    /// Object constructor;
    myPipeVisualCustom(const QString code_location = "");

    /// Accept function
    static bool acceptObject(mafCore::mafObjectBase *obj);

public Q_SLOTS:
    /// Allow to execute and update the pipeline when something change.
    /*virtual*/ void updatePipe(double t = -1);
    
protected:
    /// Object destructor.
    /* virtual */ ~myPipeVisualCustom();

private:
    bool m_ScalarVisibility; ///< Flag to activate scalar visibility.
    double m_Range[2]; ///Contour range.
};

} // mafPlugin{{ pluginName }}

#endif // MYVISUALPIPENODE_H
