#include <jni.h>
#include <stdio.h>
#include "B1.h"

JNIEXPORT jint JNICALL Java_B1_add(JNIEnv *env, jobject thisObj, jint a, jint b)
{
    printf("\n %d + %d = %d\n", a, b, (a + b));
    return (a + b);
}

JNIEXPORT jint JNICALL Java_B1_sub(JNIEnv *env, jobject thisObj, jint a, jint b)
{
    printf("\n %d - %d = %d\n", a, b, (a - b));
    return (a - b);
}

JNIEXPORT jint JNICALL Java_B1_mult(JNIEnv *env, jobject thisObj, jint a, jint b)
{
    printf("\n %d * %d = %d\n", a, b, (a * b));
    return (a * b);
}

JNIEXPORT jint JNICALL Java_B1_div(JNIEnv *env, jobject thisObj, jint a, jint b)
{
    printf("\n %d / %d = %d\n", a, b, (a / b));
    return (a / b);
}
