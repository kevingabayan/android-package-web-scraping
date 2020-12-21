# android-package-web-scraping
<h2> Web scraping all cautionary notes off of the android.app API package. </h2>
<h2> This was coded in my Fall 2020 Semester at Stony Brook University, where I took my Scripting Languages course [CSE 337]. </h2>

<h2>Background</h2>
<p>
Android is one of the most widely used mobile platform. One of its hallmarks is
that it allows users to extend its functionality by developing apps that can run on it.
Android provides numerous Application Programming Interfaces (APIs) to
facilitate app development. The set of APIs is officially maintained by the
contributors to the Android platform. The documentation of these APIs is
maintained on Android’s official website called the Android API reference
(https://developer.android.com/reference). This website is very useful for app
developers since they can refer to it while developing apps. The reference is
divided into a collection of packages. Each package offers some classes and
interfaces that encapsulate certain features of the Android platform. For example,
the android.app package (https://developer.android.com/reference/android/app/package-summary) contains
classes and interfaces that encapsulate the overall Android application model and
the fundamental building blocks of an Android app (e.g., activities and services).
These packages are vast. A user may often get lost when trying to lookup a
particular aspect of an API. For example, the documentation contains many APIs
that have special cautionary notes attached to them. These notes serve as warnings
to the user of the API. As an example consider the newKeyguardLock method in
the KeyguardManager class (https://developer.android.com/reference/android/app/KeyguardManager#newKey 
guardLock(java.lang.String)). This method has a note of warning or caution
associated with it that says that the method was deprecated in a particular version
of Android and should not be used without providing a mechanism for backward
compatibility.
<br> <br/>
Assume that a developer wants to find out all methods and fields in a class or an
interface in the android.app package that has a note of warning. Since, this would
entail a huge amount of manual labor, we need to help the developer by automating
this task. Since the entire documentation of this package is on the web, we will
write a web scraping script to automate this task.
</p>
