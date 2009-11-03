# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2007 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for http://oss.sgi.com/projects/ogl-sample/ABI/glxext.h

Generated by tools/gengl.py.
Do not modify this file.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: glxext_arb.py 935 2007-06-25 08:22:58Z Alex.Holkner $'

import ctypes
from ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
from pyglet.gl.lib import c_ptrdiff_t

if not hasattr(ctypes, 'c_int64'):
    # XXX TODO completely wrong, but at least can import.
    # Can c_longlong still be used?
    c_int64 = c_long
    c_uint64 = c_ulong

# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by tools/gengl.py.
# Wrapper for http://oss.sgi.com/projects/ogl-sample/ABI/glxext.h


# VERSION_1_3 (/usr/include/GL/glx.h:73)
# VERSION_1_4 (/usr/include/GL/glx.h:132)
# ARB_get_proc_address (/usr/include/GL/glx.h:137)
# VERSION_1_1 (/usr/include/GL/glx.h:209)
# VERSION_1_2 (/usr/include/GL/glx.h:222)
# VERSION_1_3 (/usr/include/GL/glx.h:230)
# VERSION_1_4 (/usr/include/GL/glx.h:302)
# ARB_get_proc_address (/usr/include/GL/glx.h:318)
# GLXEXT_LEGACY (/usr/include/GL/glx.h:350)
GLAPI = 0 	# GL/glxext.h:49
GLX_GLXEXT_VERSION = 11 	# GL/glxext.h:57
# VERSION_1_3 (GL/glxext.h:59)
# VERSION_1_4 (GL/glxext.h:118)
# ARB_get_proc_address (GL/glxext.h:123)
# ARB_multisample (GL/glxext.h:126)
GLX_SAMPLE_BUFFERS_ARB = 100000 	# GL/glxext.h:127
GLX_SAMPLES_ARB = 100001 	# GL/glxext.h:128
# ARB_fbconfig_float (GL/glxext.h:131)
GLX_RGBA_FLOAT_TYPE_ARB = 8377 	# GL/glxext.h:132
GLX_RGBA_FLOAT_BIT_ARB = 4 	# GL/glxext.h:133
# SGIS_multisample (GL/glxext.h:136)
GLX_SAMPLE_BUFFERS_SGIS = 100000 	# GL/glxext.h:137
GLX_SAMPLES_SGIS = 100001 	# GL/glxext.h:138
# EXT_visual_info (GL/glxext.h:141)
GLX_X_VISUAL_TYPE_EXT = 34 	# GL/glxext.h:142
GLX_TRANSPARENT_TYPE_EXT = 35 	# GL/glxext.h:143
GLX_TRANSPARENT_INDEX_VALUE_EXT = 36 	# GL/glxext.h:144
GLX_TRANSPARENT_RED_VALUE_EXT = 37 	# GL/glxext.h:145
GLX_TRANSPARENT_GREEN_VALUE_EXT = 38 	# GL/glxext.h:146
GLX_TRANSPARENT_BLUE_VALUE_EXT = 39 	# GL/glxext.h:147
GLX_TRANSPARENT_ALPHA_VALUE_EXT = 40 	# GL/glxext.h:148
GLX_NONE_EXT = 32768 	# GL/glxext.h:149
GLX_TRUE_COLOR_EXT = 32770 	# GL/glxext.h:150
GLX_DIRECT_COLOR_EXT = 32771 	# GL/glxext.h:151
GLX_PSEUDO_COLOR_EXT = 32772 	# GL/glxext.h:152
GLX_STATIC_COLOR_EXT = 32773 	# GL/glxext.h:153
GLX_GRAY_SCALE_EXT = 32774 	# GL/glxext.h:154
GLX_STATIC_GRAY_EXT = 32775 	# GL/glxext.h:155
GLX_TRANSPARENT_RGB_EXT = 32776 	# GL/glxext.h:156
GLX_TRANSPARENT_INDEX_EXT = 32777 	# GL/glxext.h:157
# SGI_swap_control (GL/glxext.h:160)
# SGI_video_sync (GL/glxext.h:163)
# SGI_make_current_read (GL/glxext.h:166)
# SGIX_video_source (GL/glxext.h:169)
# EXT_visual_rating (GL/glxext.h:172)
GLX_VISUAL_CAVEAT_EXT = 32 	# GL/glxext.h:173
GLX_SLOW_VISUAL_EXT = 32769 	# GL/glxext.h:174
GLX_NON_CONFORMANT_VISUAL_EXT = 32781 	# GL/glxext.h:175
# EXT_import_context (GL/glxext.h:179)
GLX_SHARE_CONTEXT_EXT = 32778 	# GL/glxext.h:180
GLX_VISUAL_ID_EXT = 32779 	# GL/glxext.h:181
GLX_SCREEN_EXT = 32780 	# GL/glxext.h:182
# SGIX_fbconfig (GL/glxext.h:185)
GLX_WINDOW_BIT_SGIX = 1 	# GL/glxext.h:186
GLX_PIXMAP_BIT_SGIX = 2 	# GL/glxext.h:187
GLX_RGBA_BIT_SGIX = 1 	# GL/glxext.h:188
GLX_COLOR_INDEX_BIT_SGIX = 2 	# GL/glxext.h:189
GLX_DRAWABLE_TYPE_SGIX = 32784 	# GL/glxext.h:190
GLX_RENDER_TYPE_SGIX = 32785 	# GL/glxext.h:191
GLX_X_RENDERABLE_SGIX = 32786 	# GL/glxext.h:192
GLX_FBCONFIG_ID_SGIX = 32787 	# GL/glxext.h:193
GLX_RGBA_TYPE_SGIX = 32788 	# GL/glxext.h:194
GLX_COLOR_INDEX_TYPE_SGIX = 32789 	# GL/glxext.h:195
# SGIX_pbuffer (GL/glxext.h:199)
GLX_PBUFFER_BIT_SGIX = 4 	# GL/glxext.h:200
GLX_BUFFER_CLOBBER_MASK_SGIX = 134217728 	# GL/glxext.h:201
GLX_FRONT_LEFT_BUFFER_BIT_SGIX = 1 	# GL/glxext.h:202
GLX_FRONT_RIGHT_BUFFER_BIT_SGIX = 2 	# GL/glxext.h:203
GLX_BACK_LEFT_BUFFER_BIT_SGIX = 4 	# GL/glxext.h:204
GLX_BACK_RIGHT_BUFFER_BIT_SGIX = 8 	# GL/glxext.h:205
GLX_AUX_BUFFERS_BIT_SGIX = 16 	# GL/glxext.h:206
GLX_DEPTH_BUFFER_BIT_SGIX = 32 	# GL/glxext.h:207
GLX_STENCIL_BUFFER_BIT_SGIX = 64 	# GL/glxext.h:208
GLX_ACCUM_BUFFER_BIT_SGIX = 128 	# GL/glxext.h:209
GLX_SAMPLE_BUFFERS_BIT_SGIX = 256 	# GL/glxext.h:210
GLX_MAX_PBUFFER_WIDTH_SGIX = 32790 	# GL/glxext.h:211
GLX_MAX_PBUFFER_HEIGHT_SGIX = 32791 	# GL/glxext.h:212
GLX_MAX_PBUFFER_PIXELS_SGIX = 32792 	# GL/glxext.h:213
GLX_OPTIMAL_PBUFFER_WIDTH_SGIX = 32793 	# GL/glxext.h:214
GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX = 32794 	# GL/glxext.h:215
GLX_PRESERVED_CONTENTS_SGIX = 32795 	# GL/glxext.h:216
GLX_LARGEST_PBUFFER_SGIX = 32796 	# GL/glxext.h:217
GLX_WIDTH_SGIX = 32797 	# GL/glxext.h:218
GLX_HEIGHT_SGIX = 32798 	# GL/glxext.h:219
GLX_EVENT_MASK_SGIX = 32799 	# GL/glxext.h:220
GLX_DAMAGED_SGIX = 32800 	# GL/glxext.h:221
GLX_SAVED_SGIX = 32801 	# GL/glxext.h:222
GLX_WINDOW_SGIX = 32802 	# GL/glxext.h:223
GLX_PBUFFER_SGIX = 32803 	# GL/glxext.h:224
# SGI_cushion (GL/glxext.h:227)
# SGIX_video_resize (GL/glxext.h:230)
GLX_SYNC_FRAME_SGIX = 0 	# GL/glxext.h:231
GLX_SYNC_SWAP_SGIX = 1 	# GL/glxext.h:232
# SGIX_dmbuffer (GL/glxext.h:235)
GLX_DIGITAL_MEDIA_PBUFFER_SGIX = 32804 	# GL/glxext.h:236
# SGIX_swap_group (GL/glxext.h:239)
# SGIX_swap_barrier (GL/glxext.h:242)
# SGIS_blended_overlay (GL/glxext.h:245)
GLX_BLENDED_RGBA_SGIS = 32805 	# GL/glxext.h:246
# SGIS_shared_multisample (GL/glxext.h:249)
GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS = 32806 	# GL/glxext.h:250
GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS = 32807 	# GL/glxext.h:251
# SUN_get_transparent_index (GL/glxext.h:254)
# 3DFX_multisample (GL/glxext.h:257)
GLX_SAMPLE_BUFFERS_3DFX = 32848 	# GL/glxext.h:258
GLX_SAMPLES_3DFX = 32849 	# GL/glxext.h:259
# MESA_copy_sub_buffer (GL/glxext.h:262)
# MESA_pixmap_colormap (GL/glxext.h:265)
# MESA_release_buffers (GL/glxext.h:268)
# MESA_set_3dfx_mode (GL/glxext.h:271)
GLX_3DFX_WINDOW_MODE_MESA = 1 	# GL/glxext.h:272
GLX_3DFX_FULLSCREEN_MODE_MESA = 2 	# GL/glxext.h:273
# SGIX_visual_select_group (GL/glxext.h:276)
GLX_VISUAL_SELECT_GROUP_SGIX = 32808 	# GL/glxext.h:277
# OML_swap_method (GL/glxext.h:280)
GLX_SWAP_METHOD_OML = 32864 	# GL/glxext.h:281
GLX_SWAP_EXCHANGE_OML = 32865 	# GL/glxext.h:282
GLX_SWAP_COPY_OML = 32866 	# GL/glxext.h:283
GLX_SWAP_UNDEFINED_OML = 32867 	# GL/glxext.h:284
# OML_sync_control (GL/glxext.h:287)
# NV_float_buffer (GL/glxext.h:290)
GLX_FLOAT_COMPONENTS_NV = 8368 	# GL/glxext.h:291
# SGIX_hyperpipe (GL/glxext.h:294)
GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX = 80 	# GL/glxext.h:295
GLX_BAD_HYPERPIPE_CONFIG_SGIX = 91 	# GL/glxext.h:296
GLX_BAD_HYPERPIPE_SGIX = 92 	# GL/glxext.h:297
GLX_HYPERPIPE_DISPLAY_PIPE_SGIX = 1 	# GL/glxext.h:298
GLX_HYPERPIPE_RENDER_PIPE_SGIX = 2 	# GL/glxext.h:299
GLX_PIPE_RECT_SGIX = 1 	# GL/glxext.h:300
GLX_PIPE_RECT_LIMITS_SGIX = 2 	# GL/glxext.h:301
GLX_HYPERPIPE_STEREO_SGIX = 3 	# GL/glxext.h:302
GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX = 4 	# GL/glxext.h:303
GLX_HYPERPIPE_ID_SGIX = 32816 	# GL/glxext.h:304
# MESA_agp_offset (GL/glxext.h:307)
# ARB_get_proc_address (GL/glxext.h:313)
# SGIX_video_source (GL/glxext.h:317)
XID = c_ulong 	# /usr/include/X11/X.h:71
GLXVideoSourceSGIX = XID 	# GL/glxext.h:318
# SGIX_fbconfig (GL/glxext.h:321)
GLXFBConfigIDSGIX = XID 	# GL/glxext.h:322
class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXFBConfigSGIX = POINTER(struct___GLXFBConfigRec) 	# GL/glxext.h:323
# SGIX_pbuffer (GL/glxext.h:326)
class struct_anon_199(Structure):
    __slots__ = [
        'type',
        'serial',
        'send_event',
        'display',
        'drawable',
        'event_type',
        'draw_type',
        'mask',
        'x',
        'y',
        'width',
        'height',
        'count',
    ]
class struct__XDisplay(Structure):
    __slots__ = [
    ]
struct__XDisplay._fields_ = [
    ('_opaque_struct', c_int)
]

Display = struct__XDisplay 	# /usr/include/X11/Xlib.h:519
GLXDrawable = XID 	# /usr/include/GL/glx.h:146
struct_anon_199._fields_ = [
    ('type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', GLXDrawable),
    ('event_type', c_int),
    ('draw_type', c_int),
    ('mask', c_uint),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
]

GLXBufferClobberEventSGIX = struct_anon_199 	# GL/glxext.h:340
# VERSION_1_3 (GL/glxext.h:358)
# VERSION_1_4 (GL/glxext.h:400)
# ARB_get_proc_address (GL/glxext.h:408)
# ARB_multisample (GL/glxext.h:416)
GLX_ARB_multisample = 1 	# GL/glxext.h:417
# ARB_fbconfig_float (GL/glxext.h:420)
GLX_ARB_fbconfig_float = 1 	# GL/glxext.h:421
# SGIS_multisample (GL/glxext.h:424)
GLX_SGIS_multisample = 1 	# GL/glxext.h:425
# EXT_visual_info (GL/glxext.h:428)
GLX_EXT_visual_info = 1 	# GL/glxext.h:429
# SGI_swap_control (GL/glxext.h:432)
GLX_SGI_swap_control = 1 	# GL/glxext.h:433
# GL/glxext.h:435
glXSwapIntervalSGI = _link_function('glXSwapIntervalSGI', c_int, [c_int], 'SGI_swap_control')

PFNGLXSWAPINTERVALSGIPROC = CFUNCTYPE(c_int, c_int) 	# GL/glxext.h:437
# SGI_video_sync (GL/glxext.h:440)
GLX_SGI_video_sync = 1 	# GL/glxext.h:441
# GL/glxext.h:443
glXGetVideoSyncSGI = _link_function('glXGetVideoSyncSGI', c_int, [POINTER(c_uint)], 'SGI_video_sync')

# GL/glxext.h:444
glXWaitVideoSyncSGI = _link_function('glXWaitVideoSyncSGI', c_int, [c_int, c_int, POINTER(c_uint)], 'SGI_video_sync')

PFNGLXGETVIDEOSYNCSGIPROC = CFUNCTYPE(c_int, POINTER(c_uint)) 	# GL/glxext.h:446
PFNGLXWAITVIDEOSYNCSGIPROC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_uint)) 	# GL/glxext.h:447
# SGI_make_current_read (GL/glxext.h:450)
GLX_SGI_make_current_read = 1 	# GL/glxext.h:451
class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXContext = POINTER(struct___GLXcontextRec) 	# /usr/include/GL/glx.h:155
# GL/glxext.h:453
glXMakeCurrentReadSGI = _link_function('glXMakeCurrentReadSGI', c_int, [POINTER(Display), GLXDrawable, GLXDrawable, GLXContext], 'SGI_make_current_read')

# GL/glxext.h:454
glXGetCurrentReadDrawableSGI = _link_function('glXGetCurrentReadDrawableSGI', GLXDrawable, [], 'SGI_make_current_read')

PFNGLXMAKECURRENTREADSGIPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLXDrawable, GLXContext) 	# GL/glxext.h:456
PFNGLXGETCURRENTREADDRAWABLESGIPROC = CFUNCTYPE(GLXDrawable) 	# GL/glxext.h:457
# SGIX_video_source (GL/glxext.h:460)
GLX_SGIX_video_source = 1 	# GL/glxext.h:461
# EXT_visual_rating (GL/glxext.h:472)
GLX_EXT_visual_rating = 1 	# GL/glxext.h:473
# EXT_import_context (GL/glxext.h:476)
GLX_EXT_import_context = 1 	# GL/glxext.h:477
# GL/glxext.h:479
glXGetCurrentDisplayEXT = _link_function('glXGetCurrentDisplayEXT', POINTER(Display), [], 'EXT_import_context')

# GL/glxext.h:480
glXQueryContextInfoEXT = _link_function('glXQueryContextInfoEXT', c_int, [POINTER(Display), GLXContext, c_int, POINTER(c_int)], 'EXT_import_context')

GLXContextID = XID 	# /usr/include/GL/glx.h:144
# GL/glxext.h:481
glXGetContextIDEXT = _link_function('glXGetContextIDEXT', GLXContextID, [GLXContext], 'EXT_import_context')

# GL/glxext.h:482
glXImportContextEXT = _link_function('glXImportContextEXT', GLXContext, [POINTER(Display), GLXContextID], 'EXT_import_context')

# GL/glxext.h:483
glXFreeContextEXT = _link_function('glXFreeContextEXT', None, [POINTER(Display), GLXContext], 'EXT_import_context')

PFNGLXGETCURRENTDISPLAYEXTPROC = CFUNCTYPE(POINTER(Display)) 	# GL/glxext.h:485
PFNGLXQUERYCONTEXTINFOEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXContext, c_int, POINTER(c_int)) 	# GL/glxext.h:486
PFNGLXGETCONTEXTIDEXTPROC = CFUNCTYPE(GLXContextID, GLXContext) 	# GL/glxext.h:487
PFNGLXIMPORTCONTEXTEXTPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXContextID) 	# GL/glxext.h:488
PFNGLXFREECONTEXTEXTPROC = CFUNCTYPE(None, POINTER(Display), GLXContext) 	# GL/glxext.h:489
# SGIX_fbconfig (GL/glxext.h:492)
GLX_SGIX_fbconfig = 1 	# GL/glxext.h:493
# GL/glxext.h:495
glXGetFBConfigAttribSGIX = _link_function('glXGetFBConfigAttribSGIX', c_int, [POINTER(Display), GLXFBConfigSGIX, c_int, POINTER(c_int)], 'SGIX_fbconfig')

# GL/glxext.h:496
glXChooseFBConfigSGIX = _link_function('glXChooseFBConfigSGIX', POINTER(GLXFBConfigSGIX), [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)], 'SGIX_fbconfig')

GLXPixmap = XID 	# /usr/include/GL/glx.h:145
Pixmap = XID 	# /usr/include/X11/X.h:107
# GL/glxext.h:497
glXCreateGLXPixmapWithConfigSGIX = _link_function('glXCreateGLXPixmapWithConfigSGIX', GLXPixmap, [POINTER(Display), GLXFBConfigSGIX, Pixmap], 'SGIX_fbconfig')

# GL/glxext.h:498
glXCreateContextWithConfigSGIX = _link_function('glXCreateContextWithConfigSGIX', GLXContext, [POINTER(Display), GLXFBConfigSGIX, c_int, GLXContext, c_int], 'SGIX_fbconfig')

class struct_anon_196(Structure):
    __slots__ = [
        'visual',
        'visualid',
        'screen',
        'depth',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'colormap_size',
        'bits_per_rgb',
    ]
class struct_anon_113(Structure):
    __slots__ = [
        'ext_data',
        'visualid',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'bits_per_rgb',
        'map_entries',
    ]
class struct__XExtData(Structure):
    __slots__ = [
        'number',
        'next',
        'free_private',
        'private_data',
    ]
XPointer = c_char_p 	# /usr/include/X11/Xlib.h:108
struct__XExtData._fields_ = [
    ('number', c_int),
    ('next', POINTER(struct__XExtData)),
    ('free_private', POINTER(CFUNCTYPE(c_int, POINTER(struct__XExtData)))),
    ('private_data', XPointer),
]

XExtData = struct__XExtData 	# /usr/include/X11/Xlib.h:187
VisualID = c_ulong 	# /usr/include/X11/X.h:81
struct_anon_113._fields_ = [
    ('ext_data', POINTER(XExtData)),
    ('visualid', VisualID),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('bits_per_rgb', c_int),
    ('map_entries', c_int),
]

Visual = struct_anon_113 	# /usr/include/X11/Xlib.h:270
struct_anon_196._fields_ = [
    ('visual', POINTER(Visual)),
    ('visualid', VisualID),
    ('screen', c_int),
    ('depth', c_int),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('colormap_size', c_int),
    ('bits_per_rgb', c_int),
]

XVisualInfo = struct_anon_196 	# /usr/include/X11/Xutil.h:296
# GL/glxext.h:499
glXGetVisualFromFBConfigSGIX = _link_function('glXGetVisualFromFBConfigSGIX', POINTER(XVisualInfo), [POINTER(Display), GLXFBConfigSGIX], 'SGIX_fbconfig')

# GL/glxext.h:500
glXGetFBConfigFromVisualSGIX = _link_function('glXGetFBConfigFromVisualSGIX', GLXFBConfigSGIX, [POINTER(Display), POINTER(XVisualInfo)], 'SGIX_fbconfig')

PFNGLXGETFBCONFIGATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), GLXFBConfigSGIX, c_int, POINTER(c_int)) 	# GL/glxext.h:502
PFNGLXCHOOSEFBCONFIGSGIXPROC = CFUNCTYPE(POINTER(GLXFBConfigSGIX), POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)) 	# GL/glxext.h:503
PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), GLXFBConfigSGIX, Pixmap) 	# GL/glxext.h:504
PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfigSGIX, c_int, GLXContext, c_int) 	# GL/glxext.h:505
PFNGLXGETVISUALFROMFBCONFIGSGIXPROC = CFUNCTYPE(POINTER(XVisualInfo), POINTER(Display), GLXFBConfigSGIX) 	# GL/glxext.h:506
PFNGLXGETFBCONFIGFROMVISUALSGIXPROC = CFUNCTYPE(GLXFBConfigSGIX, POINTER(Display), POINTER(XVisualInfo)) 	# GL/glxext.h:507
# SGIX_pbuffer (GL/glxext.h:510)
GLX_SGIX_pbuffer = 1 	# GL/glxext.h:511
GLXPbufferSGIX = XID 	# /usr/include/GL/glx.h:148
# GL/glxext.h:513
glXCreateGLXPbufferSGIX = _link_function('glXCreateGLXPbufferSGIX', GLXPbufferSGIX, [POINTER(Display), GLXFBConfigSGIX, c_uint, c_uint, POINTER(c_int)], 'SGIX_pbuffer')

# GL/glxext.h:514
glXDestroyGLXPbufferSGIX = _link_function('glXDestroyGLXPbufferSGIX', None, [POINTER(Display), GLXPbufferSGIX], 'SGIX_pbuffer')

# GL/glxext.h:515
glXQueryGLXPbufferSGIX = _link_function('glXQueryGLXPbufferSGIX', c_int, [POINTER(Display), GLXPbufferSGIX, c_int, POINTER(c_uint)], 'SGIX_pbuffer')

# GL/glxext.h:516
glXSelectEventSGIX = _link_function('glXSelectEventSGIX', None, [POINTER(Display), GLXDrawable, c_ulong], 'SGIX_pbuffer')

# GL/glxext.h:517
glXGetSelectedEventSGIX = _link_function('glXGetSelectedEventSGIX', None, [POINTER(Display), GLXDrawable, POINTER(c_ulong)], 'SGIX_pbuffer')

PFNGLXCREATEGLXPBUFFERSGIXPROC = CFUNCTYPE(GLXPbufferSGIX, POINTER(Display), GLXFBConfigSGIX, c_uint, c_uint, POINTER(c_int)) 	# GL/glxext.h:519
PFNGLXDESTROYGLXPBUFFERSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXPbufferSGIX) 	# GL/glxext.h:520
PFNGLXQUERYGLXPBUFFERSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), GLXPbufferSGIX, c_int, POINTER(c_uint)) 	# GL/glxext.h:521
PFNGLXSELECTEVENTSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_ulong) 	# GL/glxext.h:522
PFNGLXGETSELECTEDEVENTSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, POINTER(c_ulong)) 	# GL/glxext.h:523
# SGI_cushion (GL/glxext.h:526)
GLX_SGI_cushion = 1 	# GL/glxext.h:527
Window = XID 	# /usr/include/X11/X.h:101
# GL/glxext.h:529
glXCushionSGI = _link_function('glXCushionSGI', None, [POINTER(Display), Window, c_float], 'SGI_cushion')

PFNGLXCUSHIONSGIPROC = CFUNCTYPE(None, POINTER(Display), Window, c_float) 	# GL/glxext.h:531
# SGIX_video_resize (GL/glxext.h:534)
GLX_SGIX_video_resize = 1 	# GL/glxext.h:535
# GL/glxext.h:537
glXBindChannelToWindowSGIX = _link_function('glXBindChannelToWindowSGIX', c_int, [POINTER(Display), c_int, c_int, Window], 'SGIX_video_resize')

# GL/glxext.h:538
glXChannelRectSGIX = _link_function('glXChannelRectSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, c_int, c_int, c_int], 'SGIX_video_resize')

# GL/glxext.h:539
glXQueryChannelRectSGIX = _link_function('glXQueryChannelRectSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)], 'SGIX_video_resize')

# GL/glxext.h:540
glXQueryChannelDeltasSGIX = _link_function('glXQueryChannelDeltasSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)], 'SGIX_video_resize')

GLenum = c_uint 	# /usr/include/GL/gl.h:53
# GL/glxext.h:541
glXChannelRectSyncSGIX = _link_function('glXChannelRectSyncSGIX', c_int, [POINTER(Display), c_int, c_int, GLenum], 'SGIX_video_resize')

PFNGLXBINDCHANNELTOWINDOWSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, Window) 	# GL/glxext.h:543
PFNGLXCHANNELRECTSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, c_int, c_int, c_int) 	# GL/glxext.h:544
PFNGLXQUERYCHANNELRECTSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)) 	# GL/glxext.h:545
PFNGLXQUERYCHANNELDELTASSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)) 	# GL/glxext.h:546
PFNGLXCHANNELRECTSYNCSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, GLenum) 	# GL/glxext.h:547
# SGIX_dmbuffer (GL/glxext.h:550)
GLX_SGIX_dmbuffer = 1 	# GL/glxext.h:551
# SGIX_swap_group (GL/glxext.h:560)
GLX_SGIX_swap_group = 1 	# GL/glxext.h:561
# GL/glxext.h:563
glXJoinSwapGroupSGIX = _link_function('glXJoinSwapGroupSGIX', None, [POINTER(Display), GLXDrawable, GLXDrawable], 'SGIX_swap_group')

PFNGLXJOINSWAPGROUPSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, GLXDrawable) 	# GL/glxext.h:565
# SGIX_swap_barrier (GL/glxext.h:568)
GLX_SGIX_swap_barrier = 1 	# GL/glxext.h:569
# GL/glxext.h:571
glXBindSwapBarrierSGIX = _link_function('glXBindSwapBarrierSGIX', None, [POINTER(Display), GLXDrawable, c_int], 'SGIX_swap_barrier')

# GL/glxext.h:572
glXQueryMaxSwapBarriersSGIX = _link_function('glXQueryMaxSwapBarriersSGIX', c_int, [POINTER(Display), c_int, POINTER(c_int)], 'SGIX_swap_barrier')

PFNGLXBINDSWAPBARRIERSGIXPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int) 	# GL/glxext.h:574
PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, POINTER(c_int)) 	# GL/glxext.h:575
# SUN_get_transparent_index (GL/glxext.h:578)
GLX_SUN_get_transparent_index = 1 	# GL/glxext.h:579
# GL/glxext.h:581
glXGetTransparentIndexSUN = _link_function('glXGetTransparentIndexSUN', c_int, [POINTER(Display), Window, Window, POINTER(c_long)], 'SUN_get_transparent_index')

PFNGLXGETTRANSPARENTINDEXSUNPROC = CFUNCTYPE(c_int, POINTER(Display), Window, Window, POINTER(c_long)) 	# GL/glxext.h:583
# MESA_copy_sub_buffer (GL/glxext.h:586)
GLX_MESA_copy_sub_buffer = 1 	# GL/glxext.h:587
# GL/glxext.h:589
glXCopySubBufferMESA = _link_function('glXCopySubBufferMESA', None, [POINTER(Display), GLXDrawable, c_int, c_int, c_int, c_int], 'MESA_copy_sub_buffer')

PFNGLXCOPYSUBBUFFERMESAPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, c_int, c_int, c_int) 	# GL/glxext.h:591
# MESA_pixmap_colormap (GL/glxext.h:594)
GLX_MESA_pixmap_colormap = 1 	# GL/glxext.h:595
Colormap = XID 	# /usr/include/X11/X.h:109
# GL/glxext.h:597
glXCreateGLXPixmapMESA = _link_function('glXCreateGLXPixmapMESA', GLXPixmap, [POINTER(Display), POINTER(XVisualInfo), Pixmap, Colormap], 'MESA_pixmap_colormap')

PFNGLXCREATEGLXPIXMAPMESAPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), POINTER(XVisualInfo), Pixmap, Colormap) 	# GL/glxext.h:599
# MESA_release_buffers (GL/glxext.h:602)
GLX_MESA_release_buffers = 1 	# GL/glxext.h:603
# GL/glxext.h:605
glXReleaseBuffersMESA = _link_function('glXReleaseBuffersMESA', c_int, [POINTER(Display), GLXDrawable], 'MESA_release_buffers')

PFNGLXRELEASEBUFFERSMESAPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable) 	# GL/glxext.h:607
# MESA_set_3dfx_mode (GL/glxext.h:610)
GLX_MESA_set_3dfx_mode = 1 	# GL/glxext.h:611
# GL/glxext.h:613
glXSet3DfxModeMESA = _link_function('glXSet3DfxModeMESA', c_int, [c_int], 'MESA_set_3dfx_mode')

PFNGLXSET3DFXMODEMESAPROC = CFUNCTYPE(c_int, c_int) 	# GL/glxext.h:615
# SGIX_visual_select_group (GL/glxext.h:618)
GLX_SGIX_visual_select_group = 1 	# GL/glxext.h:619
# OML_swap_method (GL/glxext.h:622)
GLX_OML_swap_method = 1 	# GL/glxext.h:623
# OML_sync_control (GL/glxext.h:626)
GLX_OML_sync_control = 1 	# GL/glxext.h:627
# GL/glxext.h:629
glXGetSyncValuesOML = _link_function('glXGetSyncValuesOML', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')

# GL/glxext.h:630
glXGetMscRateOML = _link_function('glXGetMscRateOML', c_int, [POINTER(Display), GLXDrawable, POINTER(c_int32), POINTER(c_int32)], 'OML_sync_control')

# GL/glxext.h:631
glXSwapBuffersMscOML = _link_function('glXSwapBuffersMscOML', c_int64, [POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64], 'OML_sync_control')

# GL/glxext.h:632
glXWaitForMscOML = _link_function('glXWaitForMscOML', c_int, [POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')

# GL/glxext.h:633
glXWaitForSbcOML = _link_function('glXWaitForSbcOML', c_int, [POINTER(Display), GLXDrawable, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)], 'OML_sync_control')

PFNGLXGETSYNCVALUESOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)) 	# GL/glxext.h:635
PFNGLXGETMSCRATEOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, POINTER(c_int32), POINTER(c_int32)) 	# GL/glxext.h:636
PFNGLXSWAPBUFFERSMSCOMLPROC = CFUNCTYPE(c_int64, POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64) 	# GL/glxext.h:637
PFNGLXWAITFORMSCOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, c_int64, c_int64, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)) 	# GL/glxext.h:638
PFNGLXWAITFORSBCOMLPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, c_int64, POINTER(c_int64), POINTER(c_int64), POINTER(c_int64)) 	# GL/glxext.h:639
# NV_float_buffer (GL/glxext.h:642)
GLX_NV_float_buffer = 1 	# GL/glxext.h:643
# SGIX_hyperpipe (GL/glxext.h:646)
GLX_SGIX_hyperpipe = 1 	# GL/glxext.h:647
class struct_anon_201(Structure):
    __slots__ = [
        'pipeName',
        'networkId',
    ]
struct_anon_201._fields_ = [
    ('pipeName', c_char * 80),
    ('networkId', c_int),
]

GLXHyperpipeNetworkSGIX = struct_anon_201 	# GL/glxext.h:652
class struct_anon_202(Structure):
    __slots__ = [
        'pipeName',
        'channel',
        'participationType',
        'timeSlice',
    ]
struct_anon_202._fields_ = [
    ('pipeName', c_char * 80),
    ('channel', c_int),
    ('participationType', c_uint),
    ('timeSlice', c_int),
]

GLXHyperpipeConfigSGIX = struct_anon_202 	# GL/glxext.h:660
class struct_anon_203(Structure):
    __slots__ = [
        'pipeName',
        'srcXOrigin',
        'srcYOrigin',
        'srcWidth',
        'srcHeight',
        'destXOrigin',
        'destYOrigin',
        'destWidth',
        'destHeight',
    ]
struct_anon_203._fields_ = [
    ('pipeName', c_char * 80),
    ('srcXOrigin', c_int),
    ('srcYOrigin', c_int),
    ('srcWidth', c_int),
    ('srcHeight', c_int),
    ('destXOrigin', c_int),
    ('destYOrigin', c_int),
    ('destWidth', c_int),
    ('destHeight', c_int),
]

GLXPipeRect = struct_anon_203 	# GL/glxext.h:666
class struct_anon_204(Structure):
    __slots__ = [
        'pipeName',
        'XOrigin',
        'YOrigin',
        'maxHeight',
        'maxWidth',
    ]
struct_anon_204._fields_ = [
    ('pipeName', c_char * 80),
    ('XOrigin', c_int),
    ('YOrigin', c_int),
    ('maxHeight', c_int),
    ('maxWidth', c_int),
]

GLXPipeRectLimits = struct_anon_204 	# GL/glxext.h:671
# GL/glxext.h:674
glXQueryHyperpipeNetworkSGIX = _link_function('glXQueryHyperpipeNetworkSGIX', POINTER(GLXHyperpipeNetworkSGIX), [POINTER(Display), POINTER(c_int)], 'SGIX_hyperpipe')

# GL/glxext.h:675
glXHyperpipeConfigSGIX = _link_function('glXHyperpipeConfigSGIX', c_int, [POINTER(Display), c_int, c_int, POINTER(GLXHyperpipeConfigSGIX), POINTER(c_int)], 'SGIX_hyperpipe')

# GL/glxext.h:676
glXQueryHyperpipeConfigSGIX = _link_function('glXQueryHyperpipeConfigSGIX', POINTER(GLXHyperpipeConfigSGIX), [POINTER(Display), c_int, POINTER(c_int)], 'SGIX_hyperpipe')

# GL/glxext.h:677
glXDestroyHyperpipeConfigSGIX = _link_function('glXDestroyHyperpipeConfigSGIX', c_int, [POINTER(Display), c_int], 'SGIX_hyperpipe')

# GL/glxext.h:678
glXBindHyperpipeSGIX = _link_function('glXBindHyperpipeSGIX', c_int, [POINTER(Display), c_int], 'SGIX_hyperpipe')

# GL/glxext.h:679
glXQueryHyperpipeBestAttribSGIX = _link_function('glXQueryHyperpipeBestAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None), POINTER(None)], 'SGIX_hyperpipe')

# GL/glxext.h:680
glXHyperpipeAttribSGIX = _link_function('glXHyperpipeAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None)], 'SGIX_hyperpipe')

# GL/glxext.h:681
glXQueryHyperpipeAttribSGIX = _link_function('glXQueryHyperpipeAttribSGIX', c_int, [POINTER(Display), c_int, c_int, c_int, POINTER(None)], 'SGIX_hyperpipe')

PFNGLXQUERYHYPERPIPENETWORKSGIXPROC = CFUNCTYPE(POINTER(GLXHyperpipeNetworkSGIX), POINTER(Display), POINTER(c_int)) 	# GL/glxext.h:683
PFNGLXHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, POINTER(GLXHyperpipeConfigSGIX), POINTER(c_int)) 	# GL/glxext.h:684
PFNGLXQUERYHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(POINTER(GLXHyperpipeConfigSGIX), POINTER(Display), c_int, POINTER(c_int)) 	# GL/glxext.h:685
PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int) 	# GL/glxext.h:686
PFNGLXBINDHYPERPIPESGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int) 	# GL/glxext.h:687
PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None), POINTER(None)) 	# GL/glxext.h:688
PFNGLXHYPERPIPEATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None)) 	# GL/glxext.h:689
PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC = CFUNCTYPE(c_int, POINTER(Display), c_int, c_int, c_int, POINTER(None)) 	# GL/glxext.h:690
# MESA_agp_offset (GL/glxext.h:693)
GLX_MESA_agp_offset = 1 	# GL/glxext.h:694
# GL/glxext.h:696
glXGetAGPOffsetMESA = _link_function('glXGetAGPOffsetMESA', c_uint, [POINTER(None)], 'MESA_agp_offset')

PFNGLXGETAGPOFFSETMESAPROC = CFUNCTYPE(c_uint, POINTER(None)) 	# GL/glxext.h:698

__all__ = ['GLAPI', 'GLX_GLXEXT_VERSION', 'GLX_SAMPLE_BUFFERS_ARB',
'GLX_SAMPLES_ARB', 'GLX_RGBA_FLOAT_TYPE_ARB', 'GLX_RGBA_FLOAT_BIT_ARB',
'GLX_SAMPLE_BUFFERS_SGIS', 'GLX_SAMPLES_SGIS', 'GLX_X_VISUAL_TYPE_EXT',
'GLX_TRANSPARENT_TYPE_EXT', 'GLX_TRANSPARENT_INDEX_VALUE_EXT',
'GLX_TRANSPARENT_RED_VALUE_EXT', 'GLX_TRANSPARENT_GREEN_VALUE_EXT',
'GLX_TRANSPARENT_BLUE_VALUE_EXT', 'GLX_TRANSPARENT_ALPHA_VALUE_EXT',
'GLX_NONE_EXT', 'GLX_TRUE_COLOR_EXT', 'GLX_DIRECT_COLOR_EXT',
'GLX_PSEUDO_COLOR_EXT', 'GLX_STATIC_COLOR_EXT', 'GLX_GRAY_SCALE_EXT',
'GLX_STATIC_GRAY_EXT', 'GLX_TRANSPARENT_RGB_EXT', 'GLX_TRANSPARENT_INDEX_EXT',
'GLX_VISUAL_CAVEAT_EXT', 'GLX_SLOW_VISUAL_EXT',
'GLX_NON_CONFORMANT_VISUAL_EXT', 'GLX_SHARE_CONTEXT_EXT', 'GLX_VISUAL_ID_EXT',
'GLX_SCREEN_EXT', 'GLX_WINDOW_BIT_SGIX', 'GLX_PIXMAP_BIT_SGIX',
'GLX_RGBA_BIT_SGIX', 'GLX_COLOR_INDEX_BIT_SGIX', 'GLX_DRAWABLE_TYPE_SGIX',
'GLX_RENDER_TYPE_SGIX', 'GLX_X_RENDERABLE_SGIX', 'GLX_FBCONFIG_ID_SGIX',
'GLX_RGBA_TYPE_SGIX', 'GLX_COLOR_INDEX_TYPE_SGIX', 'GLX_PBUFFER_BIT_SGIX',
'GLX_BUFFER_CLOBBER_MASK_SGIX', 'GLX_FRONT_LEFT_BUFFER_BIT_SGIX',
'GLX_FRONT_RIGHT_BUFFER_BIT_SGIX', 'GLX_BACK_LEFT_BUFFER_BIT_SGIX',
'GLX_BACK_RIGHT_BUFFER_BIT_SGIX', 'GLX_AUX_BUFFERS_BIT_SGIX',
'GLX_DEPTH_BUFFER_BIT_SGIX', 'GLX_STENCIL_BUFFER_BIT_SGIX',
'GLX_ACCUM_BUFFER_BIT_SGIX', 'GLX_SAMPLE_BUFFERS_BIT_SGIX',
'GLX_MAX_PBUFFER_WIDTH_SGIX', 'GLX_MAX_PBUFFER_HEIGHT_SGIX',
'GLX_MAX_PBUFFER_PIXELS_SGIX', 'GLX_OPTIMAL_PBUFFER_WIDTH_SGIX',
'GLX_OPTIMAL_PBUFFER_HEIGHT_SGIX', 'GLX_PRESERVED_CONTENTS_SGIX',
'GLX_LARGEST_PBUFFER_SGIX', 'GLX_WIDTH_SGIX', 'GLX_HEIGHT_SGIX',
'GLX_EVENT_MASK_SGIX', 'GLX_DAMAGED_SGIX', 'GLX_SAVED_SGIX',
'GLX_WINDOW_SGIX', 'GLX_PBUFFER_SGIX', 'GLX_SYNC_FRAME_SGIX',
'GLX_SYNC_SWAP_SGIX', 'GLX_DIGITAL_MEDIA_PBUFFER_SGIX',
'GLX_BLENDED_RGBA_SGIS', 'GLX_MULTISAMPLE_SUB_RECT_WIDTH_SGIS',
'GLX_MULTISAMPLE_SUB_RECT_HEIGHT_SGIS', 'GLX_SAMPLE_BUFFERS_3DFX',
'GLX_SAMPLES_3DFX', 'GLX_3DFX_WINDOW_MODE_MESA',
'GLX_3DFX_FULLSCREEN_MODE_MESA', 'GLX_VISUAL_SELECT_GROUP_SGIX',
'GLX_SWAP_METHOD_OML', 'GLX_SWAP_EXCHANGE_OML', 'GLX_SWAP_COPY_OML',
'GLX_SWAP_UNDEFINED_OML', 'GLX_FLOAT_COMPONENTS_NV',
'GLX_HYPERPIPE_PIPE_NAME_LENGTH_SGIX', 'GLX_BAD_HYPERPIPE_CONFIG_SGIX',
'GLX_BAD_HYPERPIPE_SGIX', 'GLX_HYPERPIPE_DISPLAY_PIPE_SGIX',
'GLX_HYPERPIPE_RENDER_PIPE_SGIX', 'GLX_PIPE_RECT_SGIX',
'GLX_PIPE_RECT_LIMITS_SGIX', 'GLX_HYPERPIPE_STEREO_SGIX',
'GLX_HYPERPIPE_PIXEL_AVERAGE_SGIX', 'GLX_HYPERPIPE_ID_SGIX',
'GLXVideoSourceSGIX', 'GLXFBConfigIDSGIX', 'GLXFBConfigSGIX',
'GLXBufferClobberEventSGIX', 'GLX_ARB_multisample', 'GLX_ARB_fbconfig_float',
'GLX_SGIS_multisample', 'GLX_EXT_visual_info', 'GLX_SGI_swap_control',
'glXSwapIntervalSGI', 'PFNGLXSWAPINTERVALSGIPROC', 'GLX_SGI_video_sync',
'glXGetVideoSyncSGI', 'glXWaitVideoSyncSGI', 'PFNGLXGETVIDEOSYNCSGIPROC',
'PFNGLXWAITVIDEOSYNCSGIPROC', 'GLX_SGI_make_current_read',
'glXMakeCurrentReadSGI', 'glXGetCurrentReadDrawableSGI',
'PFNGLXMAKECURRENTREADSGIPROC', 'PFNGLXGETCURRENTREADDRAWABLESGIPROC',
'GLX_SGIX_video_source', 'GLX_EXT_visual_rating', 'GLX_EXT_import_context',
'glXGetCurrentDisplayEXT', 'glXQueryContextInfoEXT', 'glXGetContextIDEXT',
'glXImportContextEXT', 'glXFreeContextEXT', 'PFNGLXGETCURRENTDISPLAYEXTPROC',
'PFNGLXQUERYCONTEXTINFOEXTPROC', 'PFNGLXGETCONTEXTIDEXTPROC',
'PFNGLXIMPORTCONTEXTEXTPROC', 'PFNGLXFREECONTEXTEXTPROC', 'GLX_SGIX_fbconfig',
'glXGetFBConfigAttribSGIX', 'glXChooseFBConfigSGIX',
'glXCreateGLXPixmapWithConfigSGIX', 'glXCreateContextWithConfigSGIX',
'glXGetVisualFromFBConfigSGIX', 'glXGetFBConfigFromVisualSGIX',
'PFNGLXGETFBCONFIGATTRIBSGIXPROC', 'PFNGLXCHOOSEFBCONFIGSGIXPROC',
'PFNGLXCREATEGLXPIXMAPWITHCONFIGSGIXPROC',
'PFNGLXCREATECONTEXTWITHCONFIGSGIXPROC',
'PFNGLXGETVISUALFROMFBCONFIGSGIXPROC', 'PFNGLXGETFBCONFIGFROMVISUALSGIXPROC',
'GLX_SGIX_pbuffer', 'glXCreateGLXPbufferSGIX', 'glXDestroyGLXPbufferSGIX',
'glXQueryGLXPbufferSGIX', 'glXSelectEventSGIX', 'glXGetSelectedEventSGIX',
'PFNGLXCREATEGLXPBUFFERSGIXPROC', 'PFNGLXDESTROYGLXPBUFFERSGIXPROC',
'PFNGLXQUERYGLXPBUFFERSGIXPROC', 'PFNGLXSELECTEVENTSGIXPROC',
'PFNGLXGETSELECTEDEVENTSGIXPROC', 'GLX_SGI_cushion', 'glXCushionSGI',
'PFNGLXCUSHIONSGIPROC', 'GLX_SGIX_video_resize', 'glXBindChannelToWindowSGIX',
'glXChannelRectSGIX', 'glXQueryChannelRectSGIX', 'glXQueryChannelDeltasSGIX',
'glXChannelRectSyncSGIX', 'PFNGLXBINDCHANNELTOWINDOWSGIXPROC',
'PFNGLXCHANNELRECTSGIXPROC', 'PFNGLXQUERYCHANNELRECTSGIXPROC',
'PFNGLXQUERYCHANNELDELTASSGIXPROC', 'PFNGLXCHANNELRECTSYNCSGIXPROC',
'GLX_SGIX_dmbuffer', 'GLX_SGIX_swap_group', 'glXJoinSwapGroupSGIX',
'PFNGLXJOINSWAPGROUPSGIXPROC', 'GLX_SGIX_swap_barrier',
'glXBindSwapBarrierSGIX', 'glXQueryMaxSwapBarriersSGIX',
'PFNGLXBINDSWAPBARRIERSGIXPROC', 'PFNGLXQUERYMAXSWAPBARRIERSSGIXPROC',
'GLX_SUN_get_transparent_index', 'glXGetTransparentIndexSUN',
'PFNGLXGETTRANSPARENTINDEXSUNPROC', 'GLX_MESA_copy_sub_buffer',
'glXCopySubBufferMESA', 'PFNGLXCOPYSUBBUFFERMESAPROC',
'GLX_MESA_pixmap_colormap', 'glXCreateGLXPixmapMESA',
'PFNGLXCREATEGLXPIXMAPMESAPROC', 'GLX_MESA_release_buffers',
'glXReleaseBuffersMESA', 'PFNGLXRELEASEBUFFERSMESAPROC',
'GLX_MESA_set_3dfx_mode', 'glXSet3DfxModeMESA', 'PFNGLXSET3DFXMODEMESAPROC',
'GLX_SGIX_visual_select_group', 'GLX_OML_swap_method', 'GLX_OML_sync_control',
'glXGetSyncValuesOML', 'glXGetMscRateOML', 'glXSwapBuffersMscOML',
'glXWaitForMscOML', 'glXWaitForSbcOML', 'PFNGLXGETSYNCVALUESOMLPROC',
'PFNGLXGETMSCRATEOMLPROC', 'PFNGLXSWAPBUFFERSMSCOMLPROC',
'PFNGLXWAITFORMSCOMLPROC', 'PFNGLXWAITFORSBCOMLPROC', 'GLX_NV_float_buffer',
'GLX_SGIX_hyperpipe', 'GLXHyperpipeNetworkSGIX', 'GLXHyperpipeConfigSGIX',
'GLXPipeRect', 'GLXPipeRectLimits', 'glXQueryHyperpipeNetworkSGIX',
'glXHyperpipeConfigSGIX', 'glXQueryHyperpipeConfigSGIX',
'glXDestroyHyperpipeConfigSGIX', 'glXBindHyperpipeSGIX',
'glXQueryHyperpipeBestAttribSGIX', 'glXHyperpipeAttribSGIX',
'glXQueryHyperpipeAttribSGIX', 'PFNGLXQUERYHYPERPIPENETWORKSGIXPROC',
'PFNGLXHYPERPIPECONFIGSGIXPROC', 'PFNGLXQUERYHYPERPIPECONFIGSGIXPROC',
'PFNGLXDESTROYHYPERPIPECONFIGSGIXPROC', 'PFNGLXBINDHYPERPIPESGIXPROC',
'PFNGLXQUERYHYPERPIPEBESTATTRIBSGIXPROC', 'PFNGLXHYPERPIPEATTRIBSGIXPROC',
'PFNGLXQUERYHYPERPIPEATTRIBSGIXPROC', 'GLX_MESA_agp_offset',
'glXGetAGPOffsetMESA', 'PFNGLXGETAGPOFFSETMESAPROC']
# END GENERATED CONTENT (do not edit above this line)




