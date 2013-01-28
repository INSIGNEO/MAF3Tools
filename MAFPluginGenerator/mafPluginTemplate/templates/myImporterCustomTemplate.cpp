/*
 *  myImporterCustom.cpp
 *  mafPlugin{{ plugiNname }}
 *
 *  Created by Daniele Giunchi on 16/11/11.
 *  Copyright 2011 B3C. All rights reserved.
 *
 *  See License at: http://tiny.cc/QXJ4D
 *
 */

#include "myImporterCustom.h"

using namespace mafPlugin{{ pluginName }};
using namespace mafResources;

myImporterCustom::myImporterCustom(const QString code_location) : mafImporter(code_location) {
	
}

myImporterCustom::~myImporterCustom() {
}

bool myImporterCustom::initialize() {
	return true;
}

void myImporterCustom::execute() {
    //QMutex mutex(QMutex::Recursive);
    //QMutexLocker locker(&mutex);
    
     m_Status = mafOperationStatusExecuting;
    
    checkImportFile();
    if (m_Status == mafOperationStatusAborted) {
        cleanup();
        return;
    }
    
    QByteArray ba = filename().toAscii();
    // read data ...
    
    //uncomment
    //m_ImportedData = ... ;
    //m_ImportedData.setExternalCodecType("...");
    //QString dataType = m_ImportedData.externalDataType();

    //here set the mafDataset with the custom data
    //uncomment
    //importedData(&m_ImportedData);
    
    //set the default boundary algorithm for VTK vme
    //mafResources::mafVME * vme = qobject_cast<mafResources::mafVME *> (this->m_Output);
    //vme->dataSetCollection()->itemAtCurrentTime()->setBoundaryAlgorithmName("...");

    Q_EMIT executionEnded();
}
