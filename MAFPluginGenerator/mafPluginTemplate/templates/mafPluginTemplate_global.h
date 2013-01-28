/*
 *  mafPlugin{{ pluginName }}_Global.h
 *  mafPlugin{{ pluginName }}
 *
 *  Created by Daniele Giunchi on 30/12/11.
 *  Copyright 2011 B3C. All rights reserved.
 *
 *  See Licence at: http://tiny.cc/QXJ4D
 *
 */

#ifndef {% filter upper %}mafPlugin{{ pluginName }}_GLOBAL_H{% endfilter %}
#define {% filter upper %}mafPlugin{{ pluginName }}_GLOBAL_H{% endfilter %}

#include <QtCore/qglobal.h>

#if defined({% filter upper %}mafPlugin{{ pluginName }}_EXPORTS{% endfilter %})
#  define {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} Q_DECL_EXPORT
#else
#  define {% filter upper %}mafPlugin{{ pluginName }}SHARED_EXPORT{% endfilter %} Q_DECL_IMPORT
#endif

#endif // {% filter upper %}mafPlugin{{ pluginName }}_GLOBAL_H{% endfilter %}
