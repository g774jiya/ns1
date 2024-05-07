#include <iostream>
using namespace std;

string caesar_encrypt(string text, int shift)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
        {
            result += char(int(text[i] + shift - 65) % 26 + 65);
        }
        else
        {
            result += char(int(text[i] + shift - 97) % 26 + 97);
        }
        
   
    }
    return result;
}

string caesar_decrypt(string text, int shift)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))
        {
            result += char((text[i] - shift - 65 + 26) % 26 + 65);
        }
        else
        {
            result += char((text[i] - shift - 97 + 26) % 26 + 97);
        }
      
    }
    return result;
}

int main()
{
    string text = "ATTACKatoncE";
    int shift = 4;

    // Encryption
    string encrypted_text = caesar_encrypt(text, shift);
    cout << "Encrypted: " << encrypted_text << endl;

    // Decryption
    string decrypted_text = caesar_decrypt(encrypted_text, shift);
    cout << "Decrypted: " << decrypted_text << endl;

    return 0;
}
