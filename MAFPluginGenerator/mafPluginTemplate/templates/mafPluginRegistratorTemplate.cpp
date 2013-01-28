/*
 *  mafPluginRegistrator.cpp
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 14/12/11.
 *  Copyright 2011 B3C. All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#include "mafPluginRegistrator.h"
#include "myImporterCustom.h"

#include <mafPluginConfigurator.h>

using namespace mafCore;
using namespace mafEventBus;
using namespace mafPlugin{{ pluginName }};
using namespace mafResources;

mafPluginRegistrator::mafPluginRegistrator() {
    // Register to the mafObjectFactory the plug-in object's types.
    mafRegisterObjectAndAcceptBind(mafPlugin{{ pluginName }}::myImporterCustom);
}

mafPluginRegistrator::~mafPluginRegistrator() {
    // When the library is Un-Loaded it has to remove from the mafObjectFactory its object's types.
    mafUnregisterObjectAndAcceptUnbind(mafPlugin{{ pluginName }}::myImporterCustom);
}

void mafPluginRegistrator::registerAllObjects() {
    mafPluggedObjectsHash pluginHash;

    mafPluggedObjectInformation importerMyData("my Data Importer", "mafPlugin{{ pluginName }}::myImporterCustom");
    
    pluginHash.insertMulti("mafResources::mafImporter", importerMyData);
    
    mafEventBus::mafEventArgumentsList argList;
    argList.append(mafEventArgument(mafCore::mafPluggedObjectsHash, pluginHash));
    mafEventBusManager::instance()->notifyEvent("maf.local.resources.plugin.registerLibrary", mafEventTypeLocal, &argList);
}

void mafPluginRegistrator::registerObjects() {
    mafPluginConfigurator configurator;
    if (!configurator.parseConfigurationFile("mafPlugin{{ pluginName }}.xml")) {
        registerAllObjects();
        return;
    }
}
