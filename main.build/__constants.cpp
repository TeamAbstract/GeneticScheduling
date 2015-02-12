
#include "nuitka/prelude.hpp"

// Sentinel PyObject to be used for all our call iterator endings. It will
// become a PyCObject pointing to NULL. It's address is unique, and that's
// enough for us to use it as sentinel value.
PyObject *_sentinel_value = NULL;

PyObject *const_bytes_empty;
PyObject *const_dict_empty;
PyObject *const_int_0;
PyObject *const_int_pos_1;
PyObject *const_int_pos_2;
PyObject *const_int_pos_3;
PyObject *const_str_chr_42;
PyObject *const_str_chr_58;
PyObject *const_str_digest_5ffe39dea63ab709ee9b2ad7803fa869;
PyObject *const_str_digest_793824f36d2f864b692126bb2f20244b;
PyObject *const_str_digest_d6bc61ea1c1b607260c60c43f6a17676;
PyObject *const_str_empty;
PyObject *const_str_plain_1;
PyObject *const_str_plain_Genepool;
PyObject *const_str_plain_Generator;
PyObject *const_str_plain_Product;
PyObject *const_str_plain_ProductList;
PyObject *const_str_plain_Schedule;
PyObject *const_str_plain_Task;
PyObject *const_str_plain_Time;
PyObject *const_str_plain___all__;
PyObject *const_str_plain___builtins__;
PyObject *const_str_plain___cached__;
PyObject *const_str_plain___class__;
PyObject *const_str_plain___cmp__;
PyObject *const_str_plain___dict__;
PyObject *const_str_plain___doc__;
PyObject *const_str_plain___enter__;
PyObject *const_str_plain___exit__;
PyObject *const_str_plain___file__;
PyObject *const_str_plain___import__;
PyObject *const_str_plain___init__;
PyObject *const_str_plain___loader__;
PyObject *const_str_plain___main__;
PyObject *const_str_plain___metaclass__;
PyObject *const_str_plain___module__;
PyObject *const_str_plain___name__;
PyObject *const_str_plain___package__;
PyObject *const_str_plain___path__;
PyObject *const_str_plain___prepare__;
PyObject *const_str_plain___qualname__;
PyObject *const_str_plain_addProduct;
PyObject *const_str_plain_addSchedule;
PyObject *const_str_plain_append;
PyObject *const_str_plain_compile;
PyObject *const_str_plain_datetime;
PyObject *const_str_plain_end;
PyObject *const_str_plain_file;
PyObject *const_str_plain_fromProduct;
PyObject *const_str_plain_genepool;
PyObject *const_str_plain_generator;
PyObject *const_str_plain_getNewSchedule;
PyObject *const_str_plain_getTimeObject;
PyObject *const_str_plain_inspect;
PyObject *const_str_plain_int;
PyObject *const_str_plain_iter;
PyObject *const_str_plain_len;
PyObject *const_str_plain_metaclass;
PyObject *const_str_plain_name;
PyObject *const_str_plain_open;
PyObject *const_str_plain_print;
PyObject *const_str_plain_printPool;
PyObject *const_str_plain_product;
PyObject *const_str_plain_productList;
PyObject *const_str_plain_products;
PyObject *const_str_plain_range;
PyObject *const_str_plain_repr;
PyObject *const_str_plain_schedule;
PyObject *const_str_plain_self;
PyObject *const_str_plain_send;
PyObject *const_str_plain_site;
PyObject *const_str_plain_str;
PyObject *const_str_plain_sys;
PyObject *const_str_plain_time;
PyObject *const_str_plain_timeUtil;
PyObject *const_str_plain_type;
PyObject *const_str_plain_util;
PyObject *const_tuple_empty;
PyObject *const_tuple_none_tuple;
PyObject *const_tuple_str_chr_42_tuple;
PyObject *const_tuple_str_plain_Product_tuple;
PyObject *const_tuple_str_plain_Schedule_tuple;
PyObject *const_tuple_str_plain_self_tuple;
PyObject *const_tuple_str_plain_time_tuple;

#if defined(_WIN32) && defined(_NUITKA_EXE)
#include <Windows.h>
const unsigned char* constant_bin;
struct __initResourceConstants
{
    __initResourceConstants()
    {
        constant_bin = (const unsigned char*)LockResource(
            LoadResource(
                NULL,
                FindResource(NULL, MAKEINTRESOURCE(3), RT_RCDATA)
            )
        );
    }
} __initResourceConstants_static_initializer;
#else
extern "C" const unsigned char constant_bin[];
#endif

static void __initConstants( void )
{
    NUITKA_MAY_BE_UNUSED PyObject *exception_type, *exception_value;
    NUITKA_MAY_BE_UNUSED PyTracebackObject *exception_tb;

#ifdef _MSC_VER
    // Prevent unused warnings in case of simple programs.
    (void *)exception_type; (void *)exception_value; (void *)exception_tb;
#endif

    const_bytes_empty = UNSTREAM_BYTES( &constant_bin[ 0 ], 0 );
    const_dict_empty = _PyDict_NewPresized( 0 );
    const_int_0 = PyLong_FromUnsignedLong( 0ul );
    const_int_pos_1 = PyLong_FromUnsignedLong( 1ul );
    const_int_pos_2 = PyLong_FromUnsignedLong( 2ul );
    const_int_pos_3 = PyLong_FromUnsignedLong( 3ul );
    const_str_chr_42 = UNSTREAM_STRING( &constant_bin[ 2866 ], 1, 0 );
    const_str_chr_58 = UNSTREAM_STRING( &constant_bin[ 1374 ], 1, 0 );
    const_str_digest_5ffe39dea63ab709ee9b2ad7803fa869 = UNSTREAM_STRING( &constant_bin[ 2867 ], 13, 0 );
    const_str_digest_793824f36d2f864b692126bb2f20244b = UNSTREAM_STRING( &constant_bin[ 2880 ], 15, 0 );
    const_str_digest_d6bc61ea1c1b607260c60c43f6a17676 = UNSTREAM_STRING( &constant_bin[ 2895 ], 13, 0 );
    const_str_empty = UNSTREAM_STRING( &constant_bin[ 0 ], 0, 0 );
    const_str_plain_1 = UNSTREAM_STRING( &constant_bin[ 2908 ], 1, 0 );
    const_str_plain_Genepool = UNSTREAM_STRING( &constant_bin[ 157 ], 8, 1 );
    const_str_plain_Generator = UNSTREAM_STRING( &constant_bin[ 126 ], 9, 1 );
    const_str_plain_Product = UNSTREAM_STRING( &constant_bin[ 31 ], 7, 1 );
    const_str_plain_ProductList = UNSTREAM_STRING( &constant_bin[ 31 ], 11, 1 );
    const_str_plain_Schedule = UNSTREAM_STRING( &constant_bin[ 302 ], 8, 1 );
    const_str_plain_Task = UNSTREAM_STRING( &constant_bin[ 468 ], 4, 1 );
    const_str_plain_Time = UNSTREAM_STRING( &constant_bin[ 611 ], 4, 1 );
    const_str_plain___all__ = UNSTREAM_STRING( &constant_bin[ 2909 ], 7, 1 );
    const_str_plain___builtins__ = UNSTREAM_STRING( &constant_bin[ 2916 ], 12, 1 );
    const_str_plain___cached__ = UNSTREAM_STRING( &constant_bin[ 2928 ], 10, 1 );
    const_str_plain___class__ = UNSTREAM_STRING( &constant_bin[ 2938 ], 9, 1 );
    const_str_plain___cmp__ = UNSTREAM_STRING( &constant_bin[ 2947 ], 7, 1 );
    const_str_plain___dict__ = UNSTREAM_STRING( &constant_bin[ 2954 ], 8, 1 );
    const_str_plain___doc__ = UNSTREAM_STRING( &constant_bin[ 2962 ], 7, 1 );
    const_str_plain___enter__ = UNSTREAM_STRING( &constant_bin[ 2969 ], 9, 1 );
    const_str_plain___exit__ = UNSTREAM_STRING( &constant_bin[ 2978 ], 8, 1 );
    const_str_plain___file__ = UNSTREAM_STRING( &constant_bin[ 2986 ], 8, 1 );
    const_str_plain___import__ = UNSTREAM_STRING( &constant_bin[ 2994 ], 10, 1 );
    const_str_plain___init__ = UNSTREAM_STRING( &constant_bin[ 1439 ], 8, 1 );
    const_str_plain___loader__ = UNSTREAM_STRING( &constant_bin[ 3004 ], 10, 1 );
    const_str_plain___main__ = UNSTREAM_STRING( &constant_bin[ 3014 ], 8, 1 );
    const_str_plain___metaclass__ = UNSTREAM_STRING( &constant_bin[ 3022 ], 13, 1 );
    const_str_plain___module__ = UNSTREAM_STRING( &constant_bin[ 3035 ], 10, 1 );
    const_str_plain___name__ = UNSTREAM_STRING( &constant_bin[ 3045 ], 8, 1 );
    const_str_plain___package__ = UNSTREAM_STRING( &constant_bin[ 3053 ], 11, 1 );
    const_str_plain___path__ = UNSTREAM_STRING( &constant_bin[ 3064 ], 8, 1 );
    const_str_plain___prepare__ = UNSTREAM_STRING( &constant_bin[ 3072 ], 11, 1 );
    const_str_plain___qualname__ = UNSTREAM_STRING( &constant_bin[ 3083 ], 12, 1 );
    const_str_plain_addProduct = UNSTREAM_STRING( &constant_bin[ 1724 ], 10, 1 );
    const_str_plain_addSchedule = UNSTREAM_STRING( &constant_bin[ 1088 ], 11, 1 );
    const_str_plain_append = UNSTREAM_STRING( &constant_bin[ 3095 ], 6, 1 );
    const_str_plain_compile = UNSTREAM_STRING( &constant_bin[ 3101 ], 7, 1 );
    const_str_plain_datetime = UNSTREAM_STRING( &constant_bin[ 909 ], 8, 1 );
    const_str_plain_end = UNSTREAM_STRING( &constant_bin[ 3098 ], 3, 1 );
    const_str_plain_file = UNSTREAM_STRING( &constant_bin[ 2988 ], 4, 1 );
    const_str_plain_fromProduct = UNSTREAM_STRING( &constant_bin[ 2208 ], 11, 1 );
    const_str_plain_genepool = UNSTREAM_STRING( &constant_bin[ 187 ], 8, 1 );
    const_str_plain_generator = UNSTREAM_STRING( &constant_bin[ 217 ], 9, 1 );
    const_str_plain_getNewSchedule = UNSTREAM_STRING( &constant_bin[ 1351 ], 14, 1 );
    const_str_plain_getTimeObject = UNSTREAM_STRING( &constant_bin[ 3108 ], 13, 1 );
    const_str_plain_inspect = UNSTREAM_STRING( &constant_bin[ 3121 ], 7, 1 );
    const_str_plain_int = UNSTREAM_STRING( &constant_bin[ 443 ], 3, 1 );
    const_str_plain_iter = UNSTREAM_STRING( &constant_bin[ 3128 ], 4, 1 );
    const_str_plain_len = UNSTREAM_STRING( &constant_bin[ 3132 ], 3, 1 );
    const_str_plain_metaclass = UNSTREAM_STRING( &constant_bin[ 3024 ], 9, 1 );
    const_str_plain_name = UNSTREAM_STRING( &constant_bin[ 0 ], 4, 1 );
    const_str_plain_open = UNSTREAM_STRING( &constant_bin[ 3135 ], 4, 1 );
    const_str_plain_print = UNSTREAM_STRING( &constant_bin[ 1066 ], 5, 1 );
    const_str_plain_printPool = UNSTREAM_STRING( &constant_bin[ 1209 ], 9, 1 );
    const_str_plain_product = UNSTREAM_STRING( &constant_bin[ 64 ], 7, 1 );
    const_str_plain_productList = UNSTREAM_STRING( &constant_bin[ 64 ], 11, 1 );
    const_str_plain_products = UNSTREAM_STRING( &constant_bin[ 1760 ], 8, 1 );
    const_str_plain_range = UNSTREAM_STRING( &constant_bin[ 3139 ], 5, 1 );
    const_str_plain_repr = UNSTREAM_STRING( &constant_bin[ 2063 ], 4, 1 );
    const_str_plain_schedule = UNSTREAM_STRING( &constant_bin[ 258 ], 8, 1 );
    const_str_plain_self = UNSTREAM_STRING( &constant_bin[ 342 ], 4, 1 );
    const_str_plain_send = UNSTREAM_STRING( &constant_bin[ 3144 ], 4, 1 );
    const_str_plain_site = UNSTREAM_STRING( &constant_bin[ 3148 ], 4, 1 );
    const_str_plain_str = UNSTREAM_STRING( &constant_bin[ 1611 ], 3, 1 );
    const_str_plain_sys = UNSTREAM_STRING( &constant_bin[ 6 ], 3, 1 );
    const_str_plain_time = UNSTREAM_STRING( &constant_bin[ 766 ], 4, 1 );
    const_str_plain_timeUtil = UNSTREAM_STRING( &constant_bin[ 2806 ], 8, 1 );
    const_str_plain_type = UNSTREAM_STRING( &constant_bin[ 3152 ], 4, 1 );
    const_str_plain_util = UNSTREAM_STRING( &constant_bin[ 677 ], 4, 1 );
    const_tuple_empty = PyTuple_New( 0 );
    const_tuple_none_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_none_tuple, 0, Py_None ); Py_INCREF( Py_None );
    const_tuple_str_chr_42_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_chr_42_tuple, 0, const_str_chr_42 ); Py_INCREF( const_str_chr_42 );
    const_tuple_str_plain_Product_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_Product_tuple, 0, const_str_plain_Product ); Py_INCREF( const_str_plain_Product );
    const_tuple_str_plain_Schedule_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_Schedule_tuple, 0, const_str_plain_Schedule ); Py_INCREF( const_str_plain_Schedule );
    const_tuple_str_plain_self_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_self_tuple, 0, const_str_plain_self ); Py_INCREF( const_str_plain_self );
    const_tuple_str_plain_time_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_time_tuple, 0, const_str_plain_time ); Py_INCREF( const_str_plain_time );

    return;
}

void _initConstants( void )
{
    if ( _sentinel_value == NULL )
    {
#if PYTHON_VERSION < 300
        _sentinel_value = PyCObject_FromVoidPtr( NULL, NULL );
#else
        // The NULL value is not allowed for a capsule, so use something else.
        _sentinel_value = PyCapsule_New( (void *)27, "sentinel", NULL );
#endif
        assert( _sentinel_value );

        __initConstants();
    }
}
