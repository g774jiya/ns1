#include <iostream>
#include <string>
using namespace std;

string generateKey(string str, string key) {
    int keyLength = key.length();
    for (int i = 0; key.length() < str.length(); i++) {
        key += key[i % keyLength];
    }
    return key;
}

string vigenereCipher(string text, string key, bool encrypt) {
    string result = "";
    int shift = (encrypt) ? 1 : -1;
    for (int i = 0; i < text.length(); i++) {
        char currentChar = text[i];
        if (isalpha(currentChar)) {
            char base = isupper(currentChar) ? 'A' : 'a';
            char offset = key[i] - 'A';
            char transformedChar = (currentChar - base + shift * offset + 26) % 26 + base;
            result += transformedChar;
        } else {
            result += currentChar;
        }
    }
    return result;
}

int main() {
    string plaintext = "ATTACKTHESYSTEM";
    string keyword = "KEY";
    string key = generateKey(plaintext, keyword);

    string encryptedText = vigenereCipher(plaintext, key, true);
    string decryptedText = vigenereCipher(encryptedText, key, false);

    cout << "Original: " << plaintext << endl;
    cout << "Encrypted: " << encryptedText << endl;
    cout << "Decrypted: " << decryptedText << endl;

    return 0;
}
