/*
 *  myImporterCustom.h
 *  mafPlugin{{ pluginName }}
 *
*  Created by Daniele Giunchi on 16/11/11.
 *  Copyright 2011 B3C. All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#ifndef MYIMPORTERCUSTOM_H
#define MYIMPORTERCUSTOM_H

// Includes list
#include "mafPlugin{{ pluginName }}Definitions.h"
#include <mafImporter.h>
#include <mafProxy.h>

namespace mafPlugin{{ pluginName }} {

/**
 Class Name: myImporterCustom
 Description of the class
 */
class {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} myImporterCustom : public mafResources::mafImporter {
    Q_OBJECT
    /// typedef macro.
    mafSuperclassMacro(mafResources::mafImporter);
    
public:
    /// Object constructor.
    myImporterCustom(const QString code_location = "");

    /// open the dialog for dicom importer
    /*virtual*/ bool initialize();
    
public Q_SLOTS:
    /// Execute the resource algorithm.
    /*virtual*/ void execute();
    
protected:
    /// Object destructor.
    /* virtual */ ~myImporterCustom();
    
private:
    //uncomment
    //mafCore::mafProxy< MyData > m_ImportedData; ///< Container of the Data Source *** READ MyData is only for a test, replace with your data type***

};

} // namespace mafPlugin{{ plugiNname }}


#endif // MYIMPORTER_H
