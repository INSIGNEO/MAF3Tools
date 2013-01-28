/*
 *  myViewCustom.h
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 20/03/10.
 *  Copyright 2011 SCS-B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYVIEWCUSTOM_H
#define MYVIEWCUSTOM_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include <mafView.h>

// Class forwarding list


namespace mafPlugin{{ pluginName }} {


typedef enum {
    mafCameraDirectionX = 0,
    mafCameraDirectionY,
    mafCameraDirectionZ,
    mafCameraDirectionXNegative,
    mafCameraDirectionYNegative,
    mafCameraDirectionZNegative
} mafCameraDirection;



/**
 Class name: myView
 This is the VTK MAF3 views.
 */
class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} MyViewCustom : public mafResources::mafView {
    Q_OBJECT
    Q_PROPERTY(bool cameraParallel READ cameraParallel WRITE setCameraParallel)
    Q_PROPERTY(int cameraAxes READ cameraAxes WRITE setCameraAxes)

    /// typedef macro.
    mafSuperclassMacro(mafResources::mafView);

public Q_SLOTS:
    /// Update view.
    /*virtual*/ void updateView();

    /// Reset the visualization to show visible objects
    /*virtual*/ void resetVisualization(double *bounds = NULL);

public:
    /// Object constructor.
    MyViewCustom(const QString code_location = "");

    /// Crete view.
    /*virtual*/ bool initialize();

    /// Remove scene node passed as argument.
    /*virtual*/ void removeSceneNode(mafResources::mafSceneNode *node);

    /// Called to show/hide the node.
    /*virtual*/ void showSceneNode(mafResources::mafSceneNode *node, bool show = true);

    /// Return the camera parallel flag.
    bool cameraParallel() const;

    /// Allows to assign the camera parallel flag.
    void setCameraParallel(bool parallel = true);

    /// Return the camera axes direction.
    int cameraAxes() const;

    /// Set the camera direction.
    void setCameraAxes(int axes);

protected:
    /// Object destructor.
    /* virtual */ ~MyViewCustom();
    //my Renderer

private:
    bool m_CameraParallel; ///< Flag that store the information on camera type: true means Parallel otherwise Perspective.
    mafCameraDirection m_CameraAxesDirection; ///< Direction in which the camera is looking to.
};

/////////////////////////////////////////////////////////////
// Inline methods
/////////////////////////////////////////////////////////////

inline bool MyViewCustom::cameraParallel() const {
    return m_CameraParallel;
}

inline void MyViewCustom::setCameraParallel(bool parallel /* = true */) {
    m_CameraParallel = parallel;
}

inline int MyViewCustom::cameraAxes() const {
    return (int)m_CameraAxesDirection;
}

} //namespace mafPlugin{{ pluginName }}

#endif // MyViewCustom_H
