/*
 *  mafPlugin{{ pluginName }}Definitions.h
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 30/12/09.
 *  Copyright 2009 B3C. All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#ifndef {% filter upper %}mafPlugin{{ pluginName }}DEFINITIONS_H{% endfilter %}
#define {% filter upper %}mafPlugin{{ pluginName }}DEFINITIONS_H{% endfilter %}


// Includes list
#include "mafPlugin{{ pluginName }}_global.h"
#include <mafCoreRegistration.h>
#include <mafResourcesRegistration.h>
#include <mafResourcesDefinitions.h>

namespace mafPlugin{{ pluginName }} {

} //end namespace



#endif // {% filter upper %}mafPlugin{{ pluginName }}DEFINITIONS_H{% endfilter %}
