/*
 *  myViewCustom.cpp
 *  mafResources
 *
 *  Created by Roberto Mucci on 30/03/10.
 *  Copyright 2011 SCS-B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */


#include "MyViewCustom.h"
#include <mafSceneNode.h>

using namespace mafCore;
using namespace mafResources;
using namespace mafPlugin{{ pluginName }};
using namespace mafEventBus;

MyViewCustom::MyViewCustom(const QString code_location) : mafView(code_location),  m_CameraParallel(false), m_CameraAxesDirection(mafCameraDirectionZNegative) {

}

MyViewCustom::~MyViewCustom() {
}

bool MyViewCustom::initialize() {
    if (Superclass::initialize()) {
        // Create the instance of the Renderer
    
        //create the instance for selection pipe.

        // push camera interactor

        // Call always at the end of the initialization process to say the mafView to fill the SceneGraph
        // with the actual hierarchy present in the VME tree.
        setupSceneGraph();
        return true;
    }
    return false;
}

void MyViewCustom::showSceneNode(mafResources::mafSceneNode *node, bool show /* = true */) {
    Superclass::showSceneNode(node, show);

    if(show && m_VisibleObjects == 1) {
        resetVisualization();
    }
}

void MyViewCustom::setCameraAxes(int axes) {
    m_CameraAxesDirection = (mafCameraDirection)axes;
   
    double position[3], focalPoint[3], viewUp[3];
    switch (m_CameraAxesDirection) {
            case mafCameraDirectionX:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 1.;
                focalPoint[1] = 0.; 
                focalPoint[2] = 0.;
                viewUp[0] = 0.;
                viewUp[1] = 1.;
                viewUp[2] = 0.;
            }
                break;
            case mafCameraDirectionXNegative:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = -1.;
                focalPoint[1] = 0.; 
                focalPoint[2] = 0.;
                viewUp[0] = 0.;
                viewUp[1] = 1.;
                viewUp[2] = 0.;
            }
                break;
            case mafCameraDirectionY:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 0.;
                focalPoint[1] = 1.; 
                focalPoint[2] = 0.;
                viewUp[0] = 0.;
                viewUp[1] = 0.;
                viewUp[2] = 1.;
            }
                break;
            case mafCameraDirectionYNegative:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 0.;
                focalPoint[1] = -1.; 
                focalPoint[2] = 0.;
                viewUp[0] = 0.;
                viewUp[1] = 0.;
                viewUp[2] = 1.;
            }
                break;
            case mafCameraDirectionZ:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 0.;
                focalPoint[1] = 0.; 
                focalPoint[2] = 1.;
                viewUp[0] = 0.;
                viewUp[1] = 1.;
                viewUp[2] = 0.;
            }
                break;
            case mafCameraDirectionZNegative:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 0.;
                focalPoint[1] = 0.; 
                focalPoint[2] = -1.;
                viewUp[0] = 0.;
                viewUp[1] = 1.;
                viewUp[2] = 0.;
            }
                break;
            default:
            {
                position[0] = 0.;
                position[1] = 0.;
                position[2] = 0.;
                focalPoint[0] = 0.;
                focalPoint[1] = 0.; 
                focalPoint[2] = 1.;
                viewUp[0] = 0.;
                viewUp[1] = 1.;
                viewUp[2] = 0.;
            }
            break;
    }
    //set the camera
}

void MyViewCustom::removeSceneNode(mafResources::mafSceneNode *node) {
    if (node != NULL && node->visualPipe()) {
        //handle scenenode
    }
    Superclass::removeSceneNode(node);
}

void MyViewCustom::updateView() {

}

void MyViewCustom::resetVisualization(double *bounds) {
    //reset camera
    updateView();
}
