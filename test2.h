
typedef unsigned char   uchar2;
typedef signed char     schar2;
typedef unsigned short  ushort2;
typedef signed short    sshort2;
typedef unsigned long   ulong2;
typedef signed long     slong2;

typedef enum {
    E_0 = 0,
    E_1,
} EEE2;


typedef union _AAA2{
    unsigned short  us;
    struct {
        unsigned char   uc1;
        unsigned char   uc2;
    } sss2;
} AAA2;

typedef struct  _BBB2{
    unsigned char   b0:1;
    unsigned char   b1:1;
    unsigned char   b2:1;
    unsigned char   b3:1;
    unsigned char   b4:1;
    unsigned char   b5:1;
    unsigned char   b6:1;
    unsigned char   b7:1;
} BBB2;

typedef union _CCC2{
    BBB     bbb;
    uchar   byte;
} CCC2;
