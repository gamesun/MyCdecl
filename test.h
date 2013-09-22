
typedef unsigned char	uchar;
typedef signed char		schar;
typedef unsigned short	ushort;
typedef signed short	sshort;
typedef unsigned long	ulong;
typedef signed long		slong;

typedef enum {
	E_0 = 0,
	E_1,
} EEE;


typedef union _AAA{
	unsigned short	us;
	struct {
		unsigned char	uc1;
		unsigned char	uc2;
	} sss;
} AAA;

typedef struct	_BBB{
	unsigned char	b0:1;
	unsigned char	b1:1;
	unsigned char	b2:1;
	unsigned char	b3:1;
	unsigned char	b4:1;
	unsigned char	b5:1;
	unsigned char	b6:1;
	unsigned char	b7:1;
} BBB;

typedef union _CCC{
	BBB		bbb;
	uchar	byte;
} CCC;
